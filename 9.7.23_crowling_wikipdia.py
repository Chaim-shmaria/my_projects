# Wikipedia Image Crawler
# This script crawls Wikipedia pages, downloads large images, and organizes them in folders.

import requests
import random
import os
import urllib.parse
from bs4 import BeautifulSoup

# constants
MAX_IMAGES_FROM_OEN_PAGE = 5
MAX_FILE_NAME_LENGTH = 10


# Function to construct the file path for downloaded images
def construct_image_file_path(directory, img_url):
    # Extract the image name and extension from the URL
    img_name = img_url.rsplit("/", 1)[1]
    extension = img_url.rsplit(".", 1)[1]
    img_name = img_name.replace(".", "")
    # Create a file name based on the image name and extension
    img_name = img_name[-MAX_FILE_NAME_LENGTH]
    file_name = img_name + "." + extension
    # Combine the directory and file name to form the complete file path
    file_path = os.path.join(directory, file_name)
    return file_path


# Function to download an image from a given URL
def download_image(directory, img_url):
    # Send a request to the image URL
    response = requests.get(img_url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Construct the file path for the image
        file_path = construct_image_file_path(directory, img_url)
        try:
            # Open a file and write the image content to it
            with open(file_path, 'wb') as file:
                file.write(response.content)
        except (IOError, OSError, requests.RequestException):
            return


# Function to get the title of a Wikipedia page
def get_wiki_page_title(soup):
    # Find the 'title' tag in the HTML and extract its text
    title_tag = soup.find('title')
    page_title = title_tag.text.strip()
    # Remove any characters that are not allowed in file names
    page_title = page_title.replace(".", "")
    page_title = page_title.replace("/", "")
    return page_title


# Function to check if an image is large enough
def is_large_image(html):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # Find the first 'img' tag in the HTML
    tag = soup.find('img')
    if tag:
        # Get the 'width' and 'height' attributes from the tag
        width = tag.get('width')
        height = tag.get('height')
        if width and height:
            # Check if both width and height are greater than or equal to 50 pixels
            return int(width) >= 50 and int(height) >= 50
    return False


# Function to get random images from a Wikipedia page
def get_random_image(url, soup):
    images_urls = []
    # Define a custom lambda function to filter large images
    all_images = soup.find_all(lambda tag: is_large_image(str(tag)), class_='mw-file-element')
    # Randomly select a subset of images, up to a maximum defined by MAX_IMAGES_FROM_ONE_PAGE
    randomly_selected_images = random.sample(all_images, min(len(all_images), MAX_IMAGES_FROM_OEN_PAGE))
    for image in randomly_selected_images:
        src = image.get('src')
        if src.startswith('//'):
            src = 'https:' + src
        elif src.startswith('/'):
            src = urllib.parse.urljoin(url, src)
        images_urls.append(src)
    return images_urls


# Function to get random links from a Wikipedia page
def get_random_links(soup, visited_links, width):  # soup
    all_links = set()
    for link in soup.find_all('a', href=True):  # what is 'a', href?
        reference = link.get('href')
        wiki_prefix = reference.startswith('/wiki')
        not_special_page = ':' not in reference
        # not_special_page_2 = '#' not in reference  # credit to hezi
        not_yet_visited = reference not in visited_links
        if wiki_prefix and not_special_page and not_yet_visited:  # and not_special_page_2
            all_links.add(reference)
    all_links = list(all_links)
    random.shuffle(all_links)
    # Randomly sample a subset of links, up to a maximum defined by 'width'
    randomly_sample_links = all_links[:width]
    return randomly_sample_links


# Function to get a BeautifulSoup object from a URL
def get_page_soup_object(url):
    # Send a request to the URL and retrieve the HTML content
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup and return the soup object
        html_content = response.text
        soup_object = BeautifulSoup(html_content, 'html.parser')  # changed soup_object to soup
        return soup_object


# Function to crawl Wikipedia pages and download images
def crawl_wikipdia(url, directory, depth, width, visited_links):  # what about directory?
    soup = get_page_soup_object(url)
    # Get random large images from the current page
    images = get_random_image(url, soup)

    # Check if there are images to download (now I see it is not totally helping)
    if images:
        # Create a directory for the current Wikipedia page's images
        page_directory = os.path.join(directory, get_wiki_page_title(soup))
        os.makedirs(page_directory, exist_ok=True)

        # Iterate through the images and download them
        for image_url in images:
            download_image(page_directory, image_url)

    if depth > 0:
        # Get random links from the current page
        links = get_random_links(soup, visited_links, width)
        for link in links:
            visited_links.add(link)  # Add the current link to the visited_link
            new_url = urllib.parse.urljoin(url, link)
            crawl_wikipdia(new_url, directory, depth - 1, width, visited_links)


def main():  # temp values
    visited_links = set()
    url = 'https://en.wikipedia.org/wiki/The_Librarian_(version_control_system)'  # temp
    depth = 3
    width = 3
    directory = 'C:\\Users\\User\\Desktop\\downloaded_images'
    crawl_wikipdia(url, directory, depth, width, visited_links)


if __name__ == "__main__":
    main()
