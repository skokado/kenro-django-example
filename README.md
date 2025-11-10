# Kenro Django Example

A Django project example demonstrating a monolithic and robust (堅牢 - "Kenro") architecture.

## Setup

```bash
$ git clone https://github.com/skokado/kenro-django-example.git
$ cd kenro-django-example
$ uv sync
$ uv run manage.py runserver
```

Then open http://127.0.0.1:8000/api/docs to see the API documentation.

You will see two Django apps: `account` and `payment`, each available in `v1` and `v2` versions.

Run

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/account/' \
  -H 'accept: application/json'
```

You will see the following output in your console:

```
DEBUG: settings.cognito_app_client_id='dummy',settings.cognito_user_pool_id='dev_dummy_pool_id'
```

This demonstrates the dataclass-based settings implementation in `my_proj.settings.account.settings`.
