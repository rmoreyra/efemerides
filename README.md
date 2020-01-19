# efemerides

## Virtualenv

Activate virtualenv with `pipenv`

```bash
pipenv shell
```

# Run unit tests

```bash
python api/manage.py test efemerides.tests
```
# Run server

```bash
python api/manage.py runserver
```

# Run server in Docker

```bash
cd api/
docker-compose up
```
# Example Endpoint of Get

```bash
curl -X GET 'http://localhost:8000/api/efemerides/?day=2020-01-18'

{"hoy":"Dia del albañil","mes":{"18":["Dia del albañil"],"19":["Dia del arquero","Dia de la mandarina"]}}
```

# Without day parameter in Get

```bash
curl -X GET 'http://localhost:8000/api/efemerides/

[{"id": 4, "created": "2020-01-19T08:37:42.748Z", "modified": "2020-01-19T09:37:42.748Z", "date_efem": "2020-01-20T00:00:00Z", "msj_efem": "Dia de la mandarina"}, {"id": 3, "created": "2020-01-19T08:36:22.748Z", "modified": "2020-01-19T08:36:22.748Z", "date_efem": "2015-02-15T00:00:00Z", "msj_efem": "Dia de la hormiga"}, {"id": 2, "created": "2020-01-19T08:36:20.647Z", "modified": "2020-01-19T08:36:20.647Z", "date_efem": "2020-01-18T00:00:00Z", "msj_efem": "Dia del alba\u00f1il"}, {"id": 1, "created": "2020-01-19T08:36:20.645Z", "modified": "2020-01-19T08:33:20.743Z", "date_efem": "2020-01-19T00:00:00Z", "msj_efem": "Dia del arquero"}]
```