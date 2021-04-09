# SBSehati App using Django 3

### Installation

- `# pipenv install`
- copy .env-template to .env, change it's content accordingly

### Migrations

- generate first database
<br/>`# pipenv run python manage.py migrate`

- applying models changes
<br/>`# pipenv run python manage.py makemigrations`
<br/>`# pipenv run python manage.py migrate`

### Run Development

- `# pipenv run python manage.py runserver`
