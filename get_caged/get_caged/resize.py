import PIL
from PIL import Image
from get_caged.cage_image import CageImage


def resize_keep_aspect_ratio(cage_image: CageImage, target_width: int) -> CageImage:
    """
    Resize image to target width, but keep the aspect ratio to avoid distorting the image.

    :param cage_image: original image
    :param target_width: the width to resize to
    :return: CageImage object with the new sized image
    """
    width_percent = (target_width / float(cage_image.image_data.size[0]))
    height = int((float(cage_image.image_data.size[1]) * float(width_percent)))
    resized_image = cage_image.image_data.resize((target_width, height), PIL.Image.LANCZOS)

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


def get_new_face_coord(new_size: int, old_size: int, old_face_coord: int):
    return (new_size / old_size) * old_face_coord
