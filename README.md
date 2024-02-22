This project is a simple example of how to organize a Flask application with `deescovery`.

Here, we assume the following:

- There is a single root package called `example`.
- The app structure is flat, with individual apps like `example.users`, `example.blog`, etc. There are no nested apps.
- There are conventions for module names within packages:
  - `admin.py` is used for admin views or API endpoints. Each admin file must contain a blueprint instance.
  - `api.py` is used for API endpoints. Each API file must contain a blueprint instance.

The URL structure would be as follows:

- `/api/<module_name>/<api_endpoint>`: for API endpoints
- `/admin/<module_name>/<admin_endpoint>`: for admin views

Implementation details:

- Two blueprints should be defined to collect app and admin views.
- Two `deescovery` rules should be defined to discover blueprints from `admin.py` and `api.py` and register them with their respective blueprints.

Run the sample project:

```bash
poetry install
poetry run flask --app example.app run --reload
```

Try the following URLs:

- http://127.0.0.1:5000/api/users/support
- http://127.0.0.1:5000/admin/users/support
