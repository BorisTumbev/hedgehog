# hedgehog

Instructions to run the API:
- clone the project in a folder by your desire
- create virtualenv with "virtualenv -p python3 [env_name]"
- install all the requirements from requirements.txt with pip (pip install -r requirements.txt)
- then run migrations with ("python manage.py makemigrations" following "python manage.py migrate"
- load the dummy data in fixtures dir with "python manage.py loaddata data.json"
- and then you can run the server with "python manage.py runserver" and hit all the endpoints you desire
