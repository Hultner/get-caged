from PIL import Image

from get_caged.cage_image import CageImage
from get_caged.resize import resize_keep_aspect_ratio, create_resized_cage_image
from get_caged.crop import crop_by_face_coordinates
from get_caged import __version__


def test_version():
    assert __version__ == "0.1.0"


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


def test_crop_by_face_coordinates():
    image = Image.open("jpg_cat.png")
    cage_image = CageImage(
        id=1,
        width=400,
        height=462,
        aspect_ratio=(400 / 462),
        image_data=image,
        face_height_coord=200,
        face_width_coord=200,
    )

    new_width = 20
    new_height = 20
    resized_image, resized_by = resize_keep_aspect_ratio(image, new_width, new_height)
    resized_cage_image = create_resized_cage_image(cage_image, resized_image)
    new_cage_image = crop_by_face_coordinates(
        resized_cage_image, new_width, new_height, resized_by
    )
    # new_cage_image.image_data.save('/Users/nena/Desktop/get-caged/get_caged/tests/test_cat.png', 'PNG')
    assert new_cage_image.width == new_width
    assert new_cage_image.height == new_height
