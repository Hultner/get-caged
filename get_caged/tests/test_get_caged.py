from PIL import Image

from get_caged.resize import resize_keep_aspect_ratio
from get_caged import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_resize_keep_aspect_ratio():
    image = Image.open("jpg_cat.png")
    image_aspect_ratio = image.width / image.height

    new_width = 200
    new_height = 200
    resized_image, reized_by = resize_keep_aspect_ratio(image, new_width, new_height)
    new_aspect_ratio = resized_image.width / resized_image.height

    # some margin of error is accepted, we cant have ex. 173.16 pixels in width or height.
    assert round(image_aspect_ratio, 1) == round(new_aspect_ratio, 1)
    assert resized_image.height == new_height
    assert reized_by == "height"
