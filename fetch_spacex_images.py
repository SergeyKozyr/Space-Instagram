import requests
import os


def main():
    os.makedirs('./images/', exist_ok=False)
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()["links"]["flickr_images"]
    for image_index, image_url in enumerate(images):
        response = requests.get(image_url)
        with open(f'./images/spacex_{image_index}.jpg', 'wb') as image:
            image.write(response.content)
            print(f'Downloaded spacex_{image_index}.jpg')


if __name__ == "__main__":
    main()
