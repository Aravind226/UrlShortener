# URL Shortener (Django + DRF + Redis)

A backend URL shortening service built using Django REST Framework with Redis caching for high-performance redirects and duplicate URL optimization.

## Features
- Shorten long URLs into 6-character codes
- Automatic duplicate URL detection
- Redirect tracking with visit counts
- Top-10 most visited URLs endpoint
- Redis caching for fast lookups
- Collision-safe short code generation

## Tech Stack
- Django
- Django REST Framework
- Redis
- SQLite (default, easily switchable)

## API Endpoints

### Create short URL
POST /shorten/

Body:
{
  "originalURL": "https://example.com"
}

### Redirect
GET /<shortcode>/

### Top 10 visited URLs
GET /top/

## Setup Instructions

### Clone
git clone https://github.com/yourusername/urlshortener.git
cd urlshortener

### Create virtual environment
python -m venv env
source env/bin/activate

### Install dependencies
pip install -r requirements.txt

### Run migrations
python manage.py migrate

### Start server
python manage.py runserver

## Future Improvements
- Link expiration support
- User accounts & personal dashboards
- Rate limiting & abuse protection
- Frontend interface
