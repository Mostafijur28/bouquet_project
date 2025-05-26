# Wedding Bouquet Generator

A Django-based web application that helps users explore and generate wedding bouquet ideas. The platform allows users to browse different bouquet designs, vote on their favorites, and share bouquet inspiration with others.

## Features

- User authentication (login/register)
- Browse wedding bouquet gallery
- Like/vote system for bouquets
- Share bouquet designs
- Responsive design
- Bootstrap 5 UI components

## Technologies Used

- Python 3.11
- Django 5.0.1
- Bootstrap 5.3.0
- Font Awesome 6.0.0
- SQLite3 (Database)

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd Bouquet
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Apply database migrations:
```bash
python manage.py migrate
```

4. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Access the application:
- Main site: http://127.0.0.1:8000
- Admin panel: http://127.0.0.1:8000/admin

## Project Structure

```
bouquet_project/
├── bouquet_project/    # Project settings and main URLs
├── flowers/           # Main app directory
│   ├── templates/     # HTML templates
│   ├── models.py      # Database models
│   ├── views.py       # View logic
│   └── urls.py        # URL routing
├── static/           # Static files (CSS, JS, Images)
└── media/           # User-uploaded content
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
