# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Module for parsing webpages for image links.

Contains methods and external modules required for fetching the HTML source
code from a webpage, and then parsing through it for links leading directly
to images.
"""

from bs4 import BeautifulSoup as bs
import re
import requests


def get_html(url: str):
    """Gets HTML of a webpage.

    Takes an URL, and sends a HTTP get request to it, and returns the content
    of the request as a BeautifulSoup object.

    Args:
        url: URL to fetch the HTML from.

    Returns: Soup object of the HTML of an URL.

    """
    source = requests.get(url)
    soup = bs(source.text, 'html.parser')
    return soup


def get_links(html, regex) -> list:
    """Parse soup object of HTML for image links.

    Searches a BeautifulSoup object for every link matching to a regex
    pattern, and returns them as a list.

    Args:
        html: BeautifulSoup object of HTML.
        regex: Pattern to search for.

    Returns: List of image links on the webpage.
    """
    rex = re.compile(regex)
    links = rex.findall(str(html))
    return links
