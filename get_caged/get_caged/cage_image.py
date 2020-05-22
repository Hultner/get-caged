from pydantic import BaseModel


class CageImage(BaseModel):
    id: int
    width: int
    height: int
    aspect_ratio: float
    image_data: bytes
    face_height_coord: int
    face_width_coord: int
