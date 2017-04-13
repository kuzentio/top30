# top30

1. For run this project create virtualenv running command:
```virtualenv .env```
2. Activate virtualenvironment running:
```activate .env/bin/activate```
3. Install dependencies:
```pip install -r requirements.txt ```
4. Execute initial migrations:
```./manage.py migrate```
5. Run scrapping command:
```./manage.py grab_companies```

After command is done you can see scrapped data in sqlite database file, which is located in root of project.
Also you can see all information in django admin.