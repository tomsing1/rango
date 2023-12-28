## Starting a new django project

```bash
django-admin startproject rango_project
```

For more information on `django-admin` and the `manage.py`
script it creates, please
[consult the documentation](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-and-manage-pyy)

### Testing the development server

To get started, we test running the development server - and as we do
so, `django` will also notify us of missing components, e.g. its
database backend.

```bash
cd rango_project
python manage.py runserver
```

### Creating the SQLite database

To create the missing components, we run

```bash
python manage.py migrate
```

This command will create the `db.sqlite3` file in the project directory.

## Creating an app

A `django` application is composed of one or more apps.
Let's create the first one: `rango`:

```bash
python manage.py startapp rango
```

in a new subdirectory (`rango`) within the project folder.
Each app will define models and views, following `django's`
_model-view-template_ pattern.

To make `django` aware of the new app, we add it to the
`INSTALLED_APPS` section of the `settings.py` file within
the `rango_project` subdirectory.

### Adding a View

A View 
- handles a request that comes from the client
- executes code, and
- provides the response to the client.

