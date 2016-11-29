# django-m2agro-test
API Django.

# Requirements
- Django
- djangorestframework

``` pip install -r requirements.txt ```

# Documento
Leia a documentação para mais informações. [Documento em PDF](https://github.com/2bec/django-m2agro-test/blob/master/M2Agro-DjangoRESTAPI.pdf)

# Funcionamento
Use requests para simular e verificar o funcionamento da API.

```
$ python manage.py shell
>>> import requests
```

Crie uma função para facilitar a passagem do url no request.

```
>>> def _url(path):
...     return "http://127.0.0.1:8080/api/v1" + path
```

## Adicionando um produto
```
>>> produto = {"nome":"Diesel"}
>>> r = requests.post(_url('/produtos/'), json=produto)
>>> r
<Response [201]>
>>> r.json()
{u'updated': u'2016-11-27T23:45:37.602963Z', u'created': u'2016-11-27T23:45:37.591726Z', u'nome': u'Diesel', u'is_active': True, u'pk': 4, u'preco_medio': None}
```

## Adicionando uma safra
```
>>> import datetime
>>> data_inicio = datetime.datetime.now()
>>> data_fim = data_inicio + datetime.timedelta(days=90)
>>> safra = {"nome":"Soja 2017","data_inicio":data_inicio.isoformat(),"data_fim":data_fim.isoformat()}
>>> r = requests.post(_url("/api/v1/safras/"), json=safra)
>>> r
<Response [201]>
>>> r.json()
{u'pk': 2, u'is_active': True, u'data_inicio': u'2016-11-28T10:16:02.667346Z', u'data_fim': u'2017-02-26T10:16:02.667346Z', u'nome': u'Soja 2017'}
```

## Adicionando serviços
```
>>> preparo = {"nome":"Preparo do solo","data_inicio":data_inicio.isoformat(),"data_fim":data_inicio.isoformat(),"safra":{"pk":1,"nome":"Soja 2017","data_inicio":data_inicio.isoformat(),"data_fim":data_fim.isoformat()},"produtos":[{"produto":{"pk":1,"nome":"Diesel"},"quantidade":2,"preco":"29.90","data_compra":data_inicio.isoformat()}]}
>>> data_plantio_i = data_inicio + datetime.timedelta(days=5)
>>> data_plantio_f = data_inicio + datetime.timedelta(days=8)
>>> plantio = {"nome":"Plantio","data_inicio":data_plantio_i.isoformat(),"data_fim":data_plantio_f.isoformat(),"safra":{"pk":1,"nome":"Soja 2017","data_inicio":data_inicio.isoformat(),"data_fim":data_fim.isoformat()},"produtos":[{"produto":{"pk":2,"nome":"Adubo"},"quantidade":5,"preco":"89.90","data_compra":data_inicio.isoformat()}]}
>>> r = requests.post(_url("/api/v1/servicos/"), json=plantio)
>>> r
<Response [201]>
>>> r.json()
{u'data_fim': u'2016-12-06T10:16:02.667346Z', u'nome': u'Plantio', u'safra': {u'pk': 2, u'is_active': True, u'data_inicio': u'2016-11-28T10:16:02Z', u'data_fim': u'2017-02-26T10:16:02Z', u'nome': u'Soja 2017'}, u'data_inicio': u'2016-12-03T10:16:02.667346Z', u'pk': 15, u'produtos': [{u'preco': u'89.90', u'data_compra': u'2016-11-28T10:16:02Z', u'produto': {u'updated': u'2016-11-27T03:04:04Z', u'created': u'2016-11-27T03:04:04Z', u'nome': u'Adubo', u'is_active': False, u'pk': 2, u'preco_medio': None}, u'quantidade': u'5.00'}]}
>>> r = requests.post(_url("/api/v1/servicos/"), json=preparo)
>>> r
<Response [201]>
>>> r.json()
{u'data_fim': u'2016-11-28T10:16:02.667346Z', u'nome': u'Preparo do solo', u'safra': {u'pk': 2, u'is_active': True, u'data_inicio': u'2016-11-28T10:16:02Z', u'data_fim': u'2017-02-26T10:16:02Z', u'nome': u'Soja 2017'}, u'data_inicio': u'2016-11-28T10:16:02.667346Z', u'pk': 17, u'produtos': [{u'preco': u'29.90', u'data_compra': u'2016-11-28T10:16:02Z', u'produto': {u'updated': u'2016-11-27T03:04:04Z', u'created': u'2016-11-27T03:04:04Z', u'nome': u'Diesel', u'is_active': True, u'pk': 2, u'preco_medio': None}, u'quantidade': u'2.00'}]}
```

## Preço médio
```
>>> requests.get("http://127.0.0.1:8080/api/v1/produtos/update/preco_medio/")
<Response [200]>
>>> requests.get("http://127.0.0.1:8080/api/v1/produtos/update/preco_medio/").content
'[{"nome":"Diesel","preco_medio":"9.98","updated":"2016-11-28T15:40:57Z"}]'
```

## Update no preço médio dos produtos
Basta realizar um post com ``` mes ``` e ``` ano ```.

``` servicos = Servico.objects.filter(data_inicio__month=mes, data_inicio__year=ano) ```
Pode ser alterada para mes-1 (mês anterior). Mas a ideia foi de retornar o preco medio em determinado mês e atualizar.
```
>>> r = requests.post("http://127.0.0.1:8080/api/v1/produtos/update/preco_medio/", json={"mes":11,"ano":2016})
>>> r
<Response [200]>
>>> r.json()
[{u'updated': u'2016-11-28T15:53:12Z', u'preco_medio': u'9.98', u'nome': u'Diesel'}]
```