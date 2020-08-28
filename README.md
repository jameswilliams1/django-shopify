# Django Shopify

A Django app to display orders from Shopify and create new orders.

## Running

This project uses poetry for dependecy management. Install with:

```sh
python3 -m pip install --user --upgrade poetry
poetry shell
```

### Production

Install only production dependencies:

```sh
poetry install --no-dev
poetry shell
```

Run migrations and create a superuser:

```sh
python manage.py migrate
python manage.py createsuperuser
```

Create a `.env` file in the project base directory with at least the following values filled out:

```sh
DJANGO_SECRET_KEY=very-secret
DJANGO_ALLOWED_HOSTS=0.0.0.0,mydomain.com
```

Start the app using the script **inside the poetry env**:

```sh
./scripts/start.sh
```

_Note_: Serving static files will require traefik/nginx and whitenoise which are not currently set up.

### Local

Install all dependencies:

```sh
poetry install
poetry shell
```

Run migrations and create a superuser:

```sh
python manage.py migrate
python manage.py createsuperuser
```

Start the debug server:

```sh
python manage.py runserver
```

## Development

Follow the development installation guide above, activate a shell, then set up pre-commit:

```sh
poetry shell
pre-commit install --install-hooks
```

Run unit tests:

```sh
pytest --cov
```

## Still to Do

- Configure Django SSL settings and run `manage.py check --deploy`
- Refactor `OrderListView` to use a background task queue for accessing the Shopify API
- Set up Traefik/Whitenoise to serve static files and as a load balancer
- Update `OrderCreateForm` and `OrderCreateView` to allow for multiple line items
