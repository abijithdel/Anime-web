![web_img](https://github.com/user-attachments/assets/9e2ad6cc-0cf4-42eb-98a0-38810168f45e)

# Django Video Uploading Website

## Features
- Create and manage video categories
- Upload high-quality videos with titles, descriptions, and thumbnails
- Admin panel for easy management of videos and categories

## Setup Instructions

1. **Clone the Repository**
```
   git clone <repository_url>
   cd <repository_directory>
```
## Install Dependencies
Make sure you have **pip** and **virtualenv** installed. Then run:
```

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Apply Migrations
```
python manage.py migrate
```
## Create a Superuser
```
python manage.py createsuperuser
```
## Run the Development Server
```
python manage.py runserver
```
## Access the Admin Panel
Open your browser and go to **http://127.0.0.1:8000/admin**. Log in with the superuser credentials you created earlier.


# Managing Videos and Categories
## Uploading a Video
- Go to the admin page: http://127.0.0.1:8000/admin/
- Log in admin panel:
- Click on Content in the admin panel.
- Click Add Video.
- Enter the video details:
   Title: Enter the title of the video.
   Description: Enter a description for the video.
   Video File: Upload the video file.
   Thumbnail: Upload a thumbnail image for the video.
- Click Save to upload the video.

## Creating a Category
- Go to the admin page: http://127.0.0.1:8000/admin/
- Click on Categories in the admin panel
- Click Add Category.
- Enter the category details:
   Name: Enter the name of the category.
   Category Image: Upload an image representing the category.
- Click Save to create the category.
