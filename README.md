## Django Documentation

#### Requirements

    - Docker
    - Docker-compose
    - Git
    - Internet connection

#### Step 1: Get the Source Code

    - `git clone git@github.com:mayssalns/django.git`
 
#### Step 2: Going up the application
    
    - Inside the repository run through terminal:
        - In the first run: `docker-compose up --b -d`
        - Following: `docker-compose up`

#### Step 3: Migrate
    - `docker exec -it django_app_1 /bin/bash`
    - `cd InternLibrary`
    - `python manage.py migrate`

#### Step 4: Viewing in browser
    
    -  http://0.0.0.0:8000/
 
 
