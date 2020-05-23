import PIL
from PIL import Image
from get_caged.cage_image import CageImage


def create_resized_cage_image(cage_image: CageImage,
                              resized_image: PIL.Image.Image) -> CageImage:
    """
    Create a new CageImage from an image with a different size
    :param cage_image: original CageImage
    :param resized_image: the resized image
    :return: a CageImage with the new dimensions and image
    """

    new_face_height_coord = get_new_face_coord(resized_image.height,
                                               cage_image.height,
                                               cage_image.face_height_coord)
    new_face_width_coord = get_new_face_coord(resized_image.width,
                                              cage_image.width,
                                              cage_image.face_width_coord)

    resized_cage_image = CageImage(id=cage_image.id,
                                   width=resized_image.width,
                                   height=resized_image.height,
                                   aspect_ratio=(resized_image.width / resized_image.height),
                                   image_data=resized_image,
                                   face_height_coord=new_face_height_coord,
                                   face_width_coord=new_face_width_coord)
    return resized_cage_image


def resize_keep_aspect_ratio(image: PIL.Image.Image,
                             target_width: int,
                             target_height: int) -> (PIL.Image.Image, str):
    """
    Resize image to target width, but keep the aspect ratio to avoid distorting the image.

    :param image: original image
    :param target_width: the width we want
    :param target_height: the height we want
    :return: a tuple of resized image, and string saying if it was resized by height or width
    """
    ratio_width = target_width / image.width
    ratio_height = target_height / image.height
    if ratio_width < ratio_height:
        resized_by = "width"
        resize_width = target_width
        resize_height = round(ratio_width * image.height)
    else:
        resized_by = "height"
        resize_width = round(ratio_height * image.width)
        resize_height = target_height

    resized_image = image.resize((resize_width, resize_height), Image.LANCZOS)
    return resized_image, resized_by


def get_new_face_coord(new_size: int, old_size: int, old_face_coord: int):
    return (new_size / old_size) * old_face_coord
