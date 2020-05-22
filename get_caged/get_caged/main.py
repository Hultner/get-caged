from io import BytesIO
from starlette.responses import StreamingResponse
from fastapi import FastAPI
from PIL import Image

app = FastAPI()


@app.get("/cage")
async def get_cage_image(width: int = 0, height: int = 0):
    # TODO: exchange cat test for something like this.
    #  image = get_closest_matching_image(width, height)
    #  image = resize_image(image, width, height)
    #  image = crop_image(image, width, height)

    image = Image.open("jpg_cat.png")
    buf = BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")

