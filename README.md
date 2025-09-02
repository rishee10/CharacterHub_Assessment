# Backend Setup

First, I created a custom pagination class called `PostPagination`. This controls infinite scrolling on the frontend. By default, it returns 10 posts per page, but I’ve also allowed the client to change the page size through a query parameter, up to a maximum of 50.

Next, I built the `PostListView` using Django REST Framework’s `ListAPIView`. This endpoint returns a paginated list of posts. Each post is ordered by timestamp, with the latest posts appearing first. For each post, I also include up to 3 of its most recent comments, along with the post’s author, text, timestamp, and comment count.

```git clone https://github.com/rishee10/CharacterHub_Assessment.git```

```cd CharacterHub_Assessment```

## Create Virtual Enviroment 

```python -m venv myenv```

```venv\Scripts\activate```

## Install Dependencies

```pip install django djangorestframework```

# Migrations

```python manage.py makemigrations```

```python manage.py migrate```

## Run Server

```python manage.py runserver```

## Url

```/api/posts```

# Frontend Setup

```npm install```

## Compile and Hot-Reload for Development

```npm run dev```

## Compile and Minify for Production

```npm run build```

