# Django Basic Backend

A basic Django backend project demonstrating URL routing, HTTP responses, JSON responses, redirects, and HTML page rendering.

## 🚀 Features

* Django-based backend
* 5+ basic API endpoints
* JSON API endpoints
* Endpoint-to-endpoint redirection
* HTML page rendering
* Django URL routing
* Basic project and app structure
* Git and GitHub version control

## 🛠️ Technologies Used

* Python
* Django
* HTML
* Git
* GitHub

## 📁 Project Structure

```text
django-basic-backend/
│
├── api/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## 🔗 Available Endpoints

| Endpoint     | Method | Description              |
| ------------ | ------ | ------------------------ |
| `/`          | GET    | Home endpoint            |
| `/about/`    | GET    | About endpoint           |
| `/users/`    | GET    | Returns users as JSON    |
| `/products/` | GET    | Returns products as JSON |
| `/contact/`  | GET    | Contact information      |
| `/go-about/` | GET    | Redirects to `/about/`   |
| `/page/`     | GET    | Displays an HTML page    |

## 🔄 Request Flow

```text
Client / Browser
       ↓
config/urls.py
       ↓
api/urls.py
       ↓
views.py
       ↓
Response
       ↓
Client / Browser
```

## ↪️ Redirect Flow

The `/go-about/` endpoint redirects the user to the `/about/` endpoint.

```text
/go-about/
     ↓
go_to_about()
     ↓
redirect("about")
     ↓
/about/
     ↓
about()
     ↓
HttpResponse
```

## 🌐 HTML Page Flow

The `/page/` endpoint renders an HTML page using Django templates.

```text
/page/
   ↓
webpage()
   ↓
render(request, "index.html")
   ↓
HTML Response
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/django-basic-backend.git
cd django-basic-backend
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 5. Run migrations

```bash
python3 manage.py migrate
```

### 6. Start the development server

```bash
python3 manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 🧪 Testing the Endpoints

After starting the server, open the following URLs in your browser:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/about/
http://127.0.0.1:8000/users/
http://127.0.0.1:8000/products/
http://127.0.0.1:8000/contact/
http://127.0.0.1:8000/go-about/
http://127.0.0.1:8000/page/
```

## 📌 Learning Objectives

This project was created to understand the fundamentals of Django backend development, including:

* Django project and app structure
* URL routing
* Views
* HTTP responses
* JSON responses
* Redirects
* HTML templates
* Request-response lifecycle
* Git and GitHub workflow

## 👨‍💻 Author

**Gitesh Sharma**

B.Tech Computer Science and Engineering Student

## 📄 License

This project is created for learning and educational purposes.
