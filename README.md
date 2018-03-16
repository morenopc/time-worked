# Time Worked

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

