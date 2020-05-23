import sqlite3
import pathlib
from get_caged.cage_image import CageImage

base_path = pathlib.Path(__file__).resolve().parent


def connect():
    return sqlite3.connect(base_path / "cage.db")


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
    img_dict["image_data"] = img_dict["image_data"].tobytes()
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
