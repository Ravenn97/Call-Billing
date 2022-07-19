
 ## Template components

## Directory Structure

```
├── config
│   |___init__.py
│  
|            ├──v1──users.py
├── apps     ├──tests
│   ├── users├──schemas
│   ├── routers.py
|   ├__init__.py
|
├── utils
│   ├── __init__.py
├── .gitignore
├── __init__.py
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── wsgi.py
├── README.md
├── requirements.txt
```



## Getting Started in local

```bash
$ virtualenv venv

# Unix
$ source venv/bin/activate
# Win
$ source venv/Scripts/activate

```
build docker compose
```bash
$ docker-compose up -d --build
```
testing the test cases
```bash
$ python3 -m unittest apps/users/tests/test_calculate_block.py 
```
