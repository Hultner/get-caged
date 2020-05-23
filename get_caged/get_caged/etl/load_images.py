from pathlib import Path
from typing import Tuple
from contextlib import contextmanager

from pprint import pprint

from PIL import Image
from pydantic import BaseSettings

from get_caged.cage_image import CageImage
# from get_caged.db import initialize_db, insert_image

repository_root = Path("../../../")


# Add this to config or .env later
class ETLSettings(BaseSettings):
    unprocessed_images_folder: Path = repository_root / Path("images/unprocessed/")
    processed_images_folder: Path = repository_root / Path("images/processed/")


@contextmanager
def process_file(file_: Path):
    """
    Opens a context for processing a file,
    moves it to processed files when done if no exception occurs.
    """
    try:
        yield file_
    finally:
        destination = ETLSettings().processed_images_folder / file_.name
        with destination.open(mode="xb") as fid:
            fid.write(file_.read_bytes())
        file_.unlink()


def get_face_coords(name: str) -> Tuple[int, int]:
    return [int(coord) for coord in name.split("__")[0].split("_")]


def create_cage_img(img_path: Path) -> CageImage:
    face_x, face_y = get_face_coords(img_path.name)
    image = Image.open(img_path)
    cage_image = CageImage(
        id=None,
        width=image.width,
        height=image.height,
        aspect_ratio=(image.width / image.height),
        image_data=image,
        face_width_coord=face_x,
        face_height_coord=face_y,
    )
    # return (face_x, face_y, img_path, image, cage_image)
    return cage_image


def save_img(img: CageImage) -> None:
    "Saves the cage image to the database"
    pass


def run_processing():
    img_files = list(
        f
        for f in ETLSettings().unprocessed_images_folder.iterdir()
        if f.is_file() and f.name != ".gitkeep"
    )

    for file_ in img_files:
        try:
            with process_file(file_):
                cage_img = create_cage_img(file_)
                save_img(cage_img)
        except Exception as err:
            print(f"Error when saving file: {file_}")
            print(err)
            print("Continuing processing of files")

    return img_files


if __name__ == "__main__":
    run_processing()
