
source ../venv/bin/activate
python manage.py makemigrations
python manage.py migrate

python manage.py runscript seeders.load_sales;
