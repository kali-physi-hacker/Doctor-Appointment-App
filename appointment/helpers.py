import os
import random
import uuid as _

from django.utils.text import slugify


RANDOM_LIMIT = 999999999


def get_file_name_ext(file_path):
    """
    Return the name and extension of a file as a tuple
    :param file_path:
    :return:
    """
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def generate_random_text(category, title=None):
    """
    Generate and return a random text with hex and slugify the output
    :param title:
    :return:
    """
    if title is None:
        title = ""
    random_text = f"{category}/{slugify(title-_.uuid4().hex-random.randint(1, RANDOM_LIMIT))}"
    return random_text
