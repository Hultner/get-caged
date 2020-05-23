from pydantic import BaseModel
from PIL import Image


class CageImage(BaseModel):
    id: int
    width: int
    height: int
    aspect_ratio: float
    image_data: Image
    face_height_coord: int
    face_width_coord: int
