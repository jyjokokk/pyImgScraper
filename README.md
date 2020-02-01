# pyImgScraper

Scrapes any website with image links in it, and downloads the images to
a new or existing directory.

## TODO:

1. Write the "general" use URL scraper, that works on any page with image links.
2. Write tests
3. Look into the proper project / directory structure for a Python project.
4. Write command line options (with argparse or something similar)
5. Make sure that the downloaded image is the desired one, not for example
the thumbnail

## Possible features

1. Add option for writing / fetching companying data to the download directory.
    - Example: Text or data-type (JSON for example) file containing the URL
    to the scraped website, the date of the scrape, limitations provided for
    the scrape, etc.
2. Make possibility for crawling through the website, with given patterns.
