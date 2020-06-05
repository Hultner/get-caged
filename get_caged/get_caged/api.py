from io import BytesIO
from starlette.responses import StreamingResponse
from fastapi import FastAPI, Query

from get_caged.resize import resize_keep_aspect_ratio, create_resized_cage_image
from get_caged.crop import crop_by_face_coordinates
from get_caged.db import find_caged_image
from get_caged.target_image import TargetImageSpec

app = FastAPI()


@app.get("/cage")
async def get_cage_image(width: int = Query(..., ge=12), height: int = Query(..., ge=12)):
    target = TargetImageSpec(width=width, height=height)
    cage_image = find_caged_image(target)

    resized_image, resized_by = resize_keep_aspect_ratio(
        image=cage_image.image_data, target_width=width, target_height=height
    )
    resized_cage_image = create_resized_cage_image(cage_image, resized_image)
    new_cage_image = crop_by_face_coordinates(
        cage_image=resized_cage_image,
        target_width=width,
        target_height=height,
        resized_by=resized_by,
    )

    buf = BytesIO()
    new_cage_image.image_data.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")

