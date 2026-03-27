# Run This Project in VS Code

## 1) Open project
- Open folder: `capstone` in VS Code.
- You have:
  - `frontend/` (HTML/CSS/JS portal)
  - `backend/` (Django + MySQL starter)

## 2) Run frontend (User/Admin portals)
Open a VS Code terminal at project root and run:

```powershell
cd frontend
python -m http.server 5500
```

Then open:
- User login: `http://127.0.0.1:5500/index.html`
- Admin portal: `http://127.0.0.1:5500/admin.html`

## 3) Prepare MySQL database
Create DB in MySQL:

```sql
CREATE DATABASE medivault CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Update credentials in:
- `backend/medivault_backend/settings.py`
  - `NAME`, `USER`, `PASSWORD`, `HOST`, `PORT`

## 4) Run Django backend
Open second VS Code terminal:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend URLs:
- API health check: `http://127.0.0.1:8000/api/health/`
- Django admin: `http://127.0.0.1:8000/admin/`

## 5) Current architecture note
- Frontend pages currently store data in browser `localStorage` so they run immediately.
- Django/MySQL backend is ready and running, but frontend is not yet connected to API endpoints for records/health/tablets/appointments.

## 6) Optional next step
If you want, next step is to connect frontend pages to Django APIs so all data is stored in MySQL (instead of local browser storage).
