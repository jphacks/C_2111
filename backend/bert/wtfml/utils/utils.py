import os
from os import listdir
from os.path import isdir, isfile, join
from typing import List


def basename(path: str) -> str:
    """
    get '17asdfasdf2d_0_0.jpg' from 'train_folder/train/o/17asdfasdf2d_0_0.jpg

    Args:
        path (str): [description]

    Returns:
        str: [description]
    """
    return path.split("/")[-1]


# get 'train_folder/train/o' from 'train_folder/train/o/17asdfasdf2d_0_0.jpg'
def basefolder(path: str) -> str:
    """
    get 'train_folder/train/o' from 'train_folder/train/o/17asdfasdf2d_0_0.jpg'

    Args:
        path (str): [description]

    Returns:
        str: [description]
    """
    return "/".join(path.split("/")[:-1])


def get_image_paths(folder: str) -> List[str]:
    """
    get full image paths

    Args:
        folder (str): [description]

    Returns:
        List[str]: [description]
    """
    image_paths = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]
    if join(folder, ".DS_Store") in image_paths:
        image_paths.remove(join(folder, ".DS_Store"))
    for path in reversed(image_paths):
        if (
            basename(path)[-4:].lower() != ".jpg"
            and basename(path)[-4:].lower() != ".png"
        ):
            image_paths.remove(path)

    image_paths = sorted(image_paths)
    return image_paths


def get_subfolder_paths(folder: str) -> List[str]:
    """
    get subfolders

    Args:
        folder (str): [description]

    Returns:
        List[str]: [description]
    """
    subfolder_paths = [
        join(folder, f)
        for f in listdir(folder)
        if (isdir(join(folder, f)) and f[0] != ".")
    ]
    if join(folder, ".DS_Store") in subfolder_paths:
        subfolder_paths.remove(join(folder, ".DS_Store"))
    subfolder_paths = sorted(subfolder_paths)
    return subfolder_paths


# create an output folder if it does not already exist
def confirm_output_folder(output_folder: str) -> None:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
