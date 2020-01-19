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

{"hoy":"Dia del albañil","mes":{"18":"Dia del albañil","19":"Dia de la mandarina"}}
```
