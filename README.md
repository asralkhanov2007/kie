# KIE

A Django web application.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/asralkhanov2007/kie.git
cd kie
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 5. Create a superuser

```bash
python3 manage.py createsuperuser
```

### 6. Run the development server

```bash
python3 manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## 🛠 Built With

- [Django 6](https://www.djangoproject.com/)
- [Python 3.12](https://www.python.org/)
- [SQLite](https://www.sqlite.org/)
- [CKEditor](https://ckeditor.com/)

---

## 📁 Project Structure

```
kie/
├── accounts/       # Authentication (login, logout)
├── kie_app/        # Main application
├── kie/            # Project settings and URLs
├── templates/      # HTML templates
├── staticfiles/    # Static assets
├── media/          # Uploaded media files
├── manage.py
└── requirements.txt
```

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
