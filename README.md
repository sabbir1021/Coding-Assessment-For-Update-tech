
# How to run this project

1. Create virtual env  ```python3 -m venv ./venv```
2. Active venv ```source venv/bin/activate```
3. Install dependencies ```pip install -r requirements.txt```
4. Export .env file  ```export(xargs <.env)```
5. Run ```python manage.py makemigrations```
6. Run ```python manage.py migrate```
7. Run ```python manage.py runserver```


## How to Load data from xyz_sales_data.csv File.
```
python manage.py runscript seeders.load_sales;
```
Or 
```
bash scripts/dataload.sh
```

## Swagger URL
```
http://127.0.0.1:8000/swagger/
```

## Report

![image](https://github.com/sabbir1021/Coding-Assessment-For-Update-tech/assets/38248492/7a48c190-5b1e-424b-aaa1-fd416bcb4010)

![image](https://github.com/sabbir1021/Coding-Assessment-For-Update-tech/assets/38248492/605f5c8c-d49f-4f24-b37e-0215b9e4361c)
