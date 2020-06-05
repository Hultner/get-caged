from PIL import ImageOps

from get_caged.cage_image import CageImage

from get_caged.resize import create_resized_cage_image


def crop_by_face_coordinates(
    cage_image: CageImage, target_width: int, target_height: int, resized_by: str
) -> CageImage:
    """
    Crops image to get face as much in the center as possible, to avoid
    just getting a forehead or a chin for example.
    :param cage_image: a CageImage with an image that needs to be cropped
    :param target_width: the desired width
    :param target_height: the desired height
    :param resized_by: string saying if image was resized by height or width
    :return: CageImage object with new height and cropped to keep face
    """

    if resized_by == "height":
        # height is already target, crop width
        top = 0
        bottom = 0

        image = cage_image.image_data
        while image.width > target_width:
            if cage_image.face_height_coord < (
                image.height - cage_image.face_height_coord
            ):
                left = 0
                right = 1
            else:
                left = 1
                right = 0
            border = (left, top, right, bottom)
            image = ImageOps.crop(image, border)
    else:
        # crop height
        left = 0
        right = 0

        image = cage_image.image_data
        while image.height > target_height:
            if cage_image.face_height_coord < (
                image.height - cage_image.face_height_coord
            ):
                top = 0
                bottom = 1
            else:
                top = 1
                bottom = 0
            border = (left, top, right, bottom)
            image = ImageOps.crop(image, border)

    new_cage_image = create_resized_cage_image(cage_image, image)
    return new_cage_image
