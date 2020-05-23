from pathlib import Path
from typing import Tuple

from pprint import pprint

from pydantic import BaseSettings

# from get_caged.cage_image import CageImage

repository_root = Path("../../../")


# Add this to config or .env later
class ETLSettings(BaseSettings):
    unprocessed_images_folder: Path = repository_root / Path("images/unprocessed/")
    processed_images_folder: Path = repository_root / Path("images/processed/")


def get_face_coords(name: str) -> Tuple[int, int]:
    return [
        int(coord)
        for coord in name.split("__")[0].split("_")
    ]


def create_cage_img(img: Path) -> "CageImage":
    face_x, face_y = get_face_coords(img.name)
    return (face_x, face_y, img)


def run_processing():
    pprint(ETLSettings)
    # pprint([f for f in ETLSettings().unprocessed_images_folder.iterdir()])
    files = [
        create_cage_img(f)
        for f in ETLSettings().unprocessed_images_folder.iterdir()
        if f.is_file() and f.name != ".gitkeep"
    ]
    pprint(files)

    # for f in ETLSettings().unprocessed_images_folder.iterdir()
    return ETLSettings().unprocessed_images_folder


if __name__ == "__main__":
    run_processing()
