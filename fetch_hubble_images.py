import requests
import os
import argparse


def download_image(url, filename):
    os.makedirs('./images/', exist_ok=False)
    response = requests.get(url)
    response.raise_for_status()
    with open(f'./images/{filename}', 'wb') as image:
        image.write(response.content)


def fetch_hubble(image_id):
    hubble_url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(hubble_url)
    response.raise_for_status()
    image_url = response.json()["image_files"][-1]["file_url"]
    image_extension = os.path.splitext(image_url)[-1]
    image_name = f"hubble_{image_id}.{image_extension}"
    download_image(image_url, image_name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('collection')
    args = parser.parse_args()
    collection = args.collection
    hubble_url = f'http://hubblesite.org/api/v3/images/{collection}'
    response = requests.get(hubble_url)
    response.raise_for_status()
    for image in response.json():
        fetch_hubble(image["id"])
        print(f'Downloaded image {image["id"]}')


if __name__ == "__main__":
    main()
