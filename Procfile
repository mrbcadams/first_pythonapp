web: python manage.py migrate && python manage.py loaddata core/fixtures/sample_data.json && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
