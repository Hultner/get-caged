from PIL import Image

from get_caged.resize import resize_keep_aspect_ratio
from get_caged import __version__
from get_caged.cage_image import CageImage


def test_version():
    assert __version__ == '0.1.0'


def test_resize_keep_aspect_ratio():
    image = Image.open("jpg_cat.png")
    cage_image = CageImage(id=1,
                           width=400,
                           height=462,
                           aspect_ratio=(400/462),
                           image_data=image,
                           face_height_coord=200,
                           face_width_coord=200)
    new_width = 200
    resized_cage_image = resize_keep_aspect_ratio(cage_image, new_width)
    assert resized_cage_image.image_data.width == new_width
    assert resized_cage_image.aspect_ratio == cage_image.aspect_ratio
