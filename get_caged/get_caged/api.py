from io import BytesIO
from starlette.responses import StreamingResponse
from fastapi import FastAPI
from PIL import Image

from get_caged.cage_image import CageImage
from get_caged.resize import resize_keep_aspect_ratio, create_resized_cage_image
from get_caged.crop import crop_by_face_coordinates
from get_caged.target_image import TargetImageSpec

app = FastAPI()


@app.get("/cage")
async def get_cage_image(width: int = 0, height: int = 0):
    target = TargetImageSpec(width=width, height=height)
    cage_image = get_cage_image_from_spec(target)

    resized_image, resized_by = resize_keep_aspect_ratio(image=cage_image.image_data,
                                                         target_width=width,
                                                         target_height=height)
    resized_cage_image = create_resized_cage_image(cage_image, resized_image)
    new_cage_image = crop_by_face_coordinates(cage_image=resized_cage_image,
                                              target_width=width,
                                              target_height=height,
                                              resized_by=resized_by)

    buf = BytesIO()
    new_cage_image.image_data.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


def get_cage_image_from_spec(target: TargetImageSpec):
    image = Image.open("jpg_cat.png")
    cage_image = CageImage(id=1,
                           width=400,
                           height=462,
                           aspect_ratio=(400/462),
                           image_data=image,
                           face_height_coord=200,
                           face_width_coord=200)
    return cage_image
