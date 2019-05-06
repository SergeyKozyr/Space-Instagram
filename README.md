# Space Instagram

Three separate python scripts, two of them are for downloading space-related images, using [SpaceX](https://docs.spacexdata.com/#intro) and [Hubble](http://hubblesite.org/api/documentation) APIs.

Third one is for uploading previously downloaded images to your instagram account via instabot module.

## How to install

- Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

		pip install -r requirements.txt

- In order to login via instabot you should create .env file, containing two lines:

		LOGIN=type your instagram username here
		PASSWORD=type your password here

## Usage

**1) Download latest SpaceX rocket launch images:**
	
	python fetch_spacex_images.py

**2) Download space images from a certain collection via Hubble API:**
	
	python fetch_hubble_images.py wallpaper

"images" folder will be created and every downloaded picture will be there.


**3) Upload images to instagram:**
	
	python upload_images.py

Instabot automatically resizes images upon uploading them, so each file will have a resized duplicate in "images" folder.

**4) The result:**

![instagram](https://i.paste.pics/1a8b7f044fe25a7a4acf7a175e0eaaaa.png)

## Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.
