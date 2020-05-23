import sqlite3
import pathlib
import io

from PIL import Image

from get_caged.cage_image import CageImage
from get_caged.target_image import TargetImageSpec

base_path = pathlib.Path(__file__).resolve().parent


def connect():
    return sqlite3.connect(base_path / "cage.db")


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def initialize_db():
    conn = connect()
    c = conn.cursor()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS nicholas_cage_images
            (id integer PRIMARY KEY,
            width integer NOT NULL,
            height integer NOT NULL,
            aspect_ratio float NOT NULL,
            image_data blob NOT NULL,
            face_height_coord integer NOT NULL,
            face_width_coord integer NOT NULL)
        """
    )

    conn.commit()


def insert_image(img: CageImage):
    conn = connect()
    c = conn.cursor()
    # Discard the id which is None for new images
    img_dict = img.dict()
    stream = io.BytesIO()
    img_dict["image_data"].save(stream, format="JPEG")
    img_dict["image_data"] = stream.getvalue()
    # If we need we can update the PIL object to bytes here
    _, *insert_data = img_dict.values()
    insert_data = tuple(insert_data)

    print(f"inserting data: {img}")
    c.execute(
        """
        INSERT INTO nicholas_cage_images
        (width,
         height,
         aspect_ratio,
         image_data,
         face_height_coord,
         face_width_coord
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        insert_data,
    )
    conn.commit()
    conn.close()


def find_caged_image(target: TargetImageSpec) -> CageImage:
    "Queries the best match based on target"

    conn = connect()
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute(
        """
        select
                *
        from nicholas_cage_images
        where
                nicholas_cage_images.width > :width
                and nicholas_cage_images.height > :height
        order by
                ABS(nicholas_cage_images.aspect_ratio - :aspect_ratio) ASC
        limit 1
        """,
        {**target.dict(), "aspect_ratio": target.aspect_ratio},
    )
    item = c.fetchone()

    if item is None:
        # If no image with higher resolution is found
        c.execute(
            """
            select
                    *
            from nicholas_cage_images
            order by
                    ABS(nicholas_cage_images.aspect_ratio - :aspect_ratio) ASC
            limit 1
            """,
            {**target.dict(), "aspect_ratio": target.aspect_ratio},
        )
        item = c.fetchone()

    conn.close()

    item['image_data'] = Image.open(io.BytesIO(item['image_data']))

    return CageImage(**item)
