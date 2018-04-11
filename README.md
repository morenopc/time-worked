# Time Worked

## Approach

In columns there should be employees, in rows there should be projects and in the cells in the middle there should be time that a given employee spent working on the given project. Only the projects and employees which worked on a given day should be presented. The table is rendered for one day which by default is yesterday.

So for example:
```
2018-03-13 (yesterday) Time Table
+-----------+------+--------+------+------+
|           | Noah | Olivia | Liam | Ava  |
+-----------+------+--------+------+------+
| Project A | 40h  | 20h    |   -  | 120h |
+-----------+------+--------+------+------+
| Project B | 8h   | 40h    | 160h |   -  |
+-----------+------+--------+------+------+
| Project C |   -  | 240h   | 40h  | 10h  |
+-----------+------+--------+------+------+
```

## Resources
- Python 3.6.4 / Django 2.0.3
- Django REST framework 3.7.7 (and other apps)

## Setup development 

### Install python 3.6.4 with pyenv

Follow the  Installation / Update / Uninstallation at [https://github.com/yyuu/pyenv-installer#installation--update--uninstallation](https://github.com/yyuu/pyenv-installer#installation--update--uninstallation)

```
$ pyenv update
```
Install python 3.6.4
```
$ pyenv install 3.6.4
$ pyenv global 3.6.4
$ pyenv versions
  system
* 3.6.4 (set by /home/moreno/.pyenv/version)
$ python -V
Python 3.6.4
```

### Run local server

```
$ python -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py runserver
```

## Usage

### Get default yesterday table

```
http://localhost:8000/
```

### Get filtered by day table

```
http://localhost:8000/?d=2018-03-20
```
