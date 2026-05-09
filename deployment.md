# Railway Deployment Guide for Livo Project

This guide explains how to deploy this Django project to [Railway](https://railway.app/).

## Prerequisites
1. A Railway account.
2. Railway CLI installed (optional, but recommended).
3. Your project pushed to a GitHub repository.

## Steps to Deploy

### 1. Project Configuration (Already Done)
The project has been configured with the following for production:
- **WhiteNoise**: For serving static files.
- **dj-database-url**: For connecting to Railway's PostgreSQL.
- **Gunicorn**: As the production WSGI server.
- **Procfile**: Tells Railway how to run the app.
- **requirements.txt**: Updated with production dependencies.

### 2. Create a New Project on Railway
1. Go to [Railway Dashboard](https://railway.app/dashboard).
2. Click **+ New Project**.
3. Select **Deploy from GitHub repo**.
4. Choose this repository.

### 3. Add a Database (Option A: PostgreSQL - Recommended)
1. In your Railway project, click **+ Add** -> **Database** -> **Add PostgreSQL**.
2. Railway will automatically provide a `DATABASE_URL`.

### 3. Add a Database (Option B: SQLite with Persistence)
1. In your Railway project, click **+ Add** -> **Volume**.
2. Mount the volume at `/data`.
3. In your service's **Variables**, set `DATABASE_URL` to `sqlite:////data/db.sqlite3`.
   *Note: Without a Volume, your database will reset on every deploy.*

### 4. Configure Environment Variables
Go to the **Variables** tab of your service in Railway and add the following:

| Variable | Value | Description |
| :--- | :--- | :--- |
| `DATABASE_URL` | (Auto-populated) | PostgreSQL connection string |
| `SECRET_KEY` | `your-very-secret-key` | A long random string for Django security |
| `DEBUG` | `False` | Set to `False` for production |
| `ALLOWED_HOSTS` | `your-app-name.up.railway.app` | Your Railway domain (or `*`) |
| `PYTHON_VERSION` | `3.12` | Recommended Python version |

### 5. Deployment Configuration
The project includes a `railway.json` file which automatically:
- Runs database migrations before deployment (`preDeploy`).
- Sets the start command for the web server.

If you want to run migrations manually, you can use the Railway CLI:
```bash
railway run python livo/manage.py migrate
```

### 6. Static Files
The project is configured to use WhiteNoise. Static files will be collected automatically during the build process.

## Troubleshooting
- **Database Errors**: Ensure `psycopg2-binary` is in `requirements.txt`.
- **Static Files not loading**: Check if `whitenoise` is in `MIDDLEWARE` in `settings.py`.
- **Application Error**: Check the **Logs** tab in Railway for specific error messages.
