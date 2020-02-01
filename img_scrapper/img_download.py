# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Module for downloading image files from URLs.

Contains the functions and imported modules required for downloading image
file(s) from it's URL.
"""
from io import BytesIO
from PIL import Image
import requests


def download_image(url: str, f_name: str = "", file_format: str = ""):
    """Downloads an image from an URL.

    Makes an HTTP get request to an URL, and saves it's content as an image
    file with the optional arguments f_name and file_format as it's

    Args:
        url: URL to the image.
        f_name: Filename the image is saved as.
        file_format: What file format is the image saved as.

    """
    resp = requests.get(url)
    # BytesIO gives the bytes object in resp the required
    # methods to work with Image.open
    img = Image.open(BytesIO(resp.content))
    img.save(f_name, file_format)


def download_from_list(url_list: list, img_format: str, f_name: str = ""):
    """Downloads all images from a list of URLs.

    Takes a list of image URLs, and tries to download the image file from each
    of them. Also takes optional filename and image format arguments, which if
    empty, result in using filename and format extracted from the URL.
    The filename will be appended with a running number.

    Args:
        url_list: List of IMG urls.
        f_name: Filename to use as the basename.
        img_format: Image format to be saved as.

    """
    if f_name == "":
        f_name = "ScrapedImg"
    for i in range(len(url_list)):
        fname = f"{f_name}_{i}.{img_format}"
        download_image(url_list[i], fname, img_format)

