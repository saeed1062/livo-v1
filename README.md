# Django Lab Project

## Setup

```bash
git clone https://github.com/saeed1062/livo-v1/
cd livo-v1

python -m venv .venv
.venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

## Run

```bash
cd livo
python manage.py runserver
```

Open: http://127.0.0.1:8000/

## Database

* SQLite database (`db.sqlite3`) is already included
* Contains sample data (including users)
* Run migrations only if needed:

```bash
python manage.py migrate
```

