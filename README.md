# django-m2agro-test
API Django.

# Funcionamento
Use requests para simular e verificar o funcionamento da API.

```
$ python manage.py shell
>>> import requests
```

Crie uma função para facilitar a passagem do url no request.

```
>>> def _url(path):
...     return "http://127.0.0.1:8080" + path
```

## Adicionando um produto
```
>>> produto = {"nome":"Diesel"}
>>> r = requests.post(_url('/produtos/'), json=produto)
>>> r
<Response [201]>
>>> r.json()
{u'updated': u'2016-11-27T23:45:37.602963Z', u'created': u'2016-11-27T23:45:37.591726Z', u'nome': u'Diesel', u'is_active': False, u'pk': 4, u'preco_medio': None}
```