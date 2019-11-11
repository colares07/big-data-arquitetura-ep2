# Arquitetura - trabalho - EP2 

Esse projeto tem como objetivo realizar integrações entre aplicações distintas por intermédio de uma fila.

#### Estrutura de containers:  

![](/ep2.png)


#### Modelagem das images:
![](/ep2-container.png)


## Executar a aplicação 

Para executar o orquestrador 

```
docker-compose up
```

Para a execução

```
docker-compose down
```

## API Rest

### Requisição

#### Criar usuário

```curl
curl -X POST \
  http://localhost:5000/api/v1/user \
   -H 'Content-Type: application/json' \
  -d '{
	"id" : 1,
	"name": "fulano de tal",
	"age" : 19
}'
```

#### Resposta

```json
{
    "event": "create",
    "metadata": {
        "id": 1,
        "name": "fulano de tal",
        "age": 19
    }
}
```

#### Atualizar o usuário

```curl
curl -X PUT \
  http://localhost:5000/api/v1/user/1 \
   -H 'Content-Type: application/json' \
  -d '{
	"name": "Fulano de Tal",
	"age" : 22
}'
```

#### Resposta

```json
{
    "event": "update",
    "metadata": {
        "name": "Fulano de Tal",
        "age": 22,
        "id": 1
    }
}
```

#### Atualizar o usuário

```curl
curl -X DELETE http://localhost:6000/api/v1/user/1 
```

#### Resposta

```json
{
    "event": "delete",
    "metadata": {
        "id": 1
    }
}
```

## Os schema dos bancos de dados

### Event-store
Utiliza o banco **Mongo** para ser responsavel por armazenar os eventos executados:
* URL: **http://localhost:27017**
* Database: **EP2**
* Collection: **event-store**

```json
{
    "_id" : ObjectId("5dc06ae6c69835136b575a74"),
    "event" : "create",
    "metadata" : {
        "id" : 1,
        "name" : "fulano de tal",
        "idade" : 19
    }
}
```

### Accountant
Utiliza o banco **Redis** para ser responsavel por armazenar quantidade de eventos realizados:

* URL: **http://localhost:6670**
* Database: **db0**

```json
user_create : 0
user_delete : 0
user_update : 0
```

### Fact
Também utiliza o banco **Redis** mas para ser responsavel pelo armazenar dos registros atuais: 
* URL: **http://localhost:6677**
* Database: **db0**

```json
1 : {
        "name": "Fulano de Tal",
        "age": 22,
        "id":  1
    }
```

## Obter dados 
Os dados estão disponíveis pelas seguintes APIs 

### Event-store

#### Solicitação:

```curl
curl -X GET http://localhost:9000/api/v1/event-store

```

#### Resposta:

``` json
[
    {
        "_id": {
            "$oid": "5dc8b6a792549023f29ffd16"
        },
        "event": "create",
        "metadata": {
            "id": 1,
            "name": "fulano de tal",
            "idade": 19
        },
        "datetime": {
            "$date": 1573435047585
        }
    }
]
```

### Accountant

#### Solicitação:

```curl
curl -X GET http://localhost:9001/api/v1/accountant

```
#### Resposta:

``` json
{
    "user_create": 1,
    "user_update": 0,
    "user_delete": 0
}
```

### Fact

#### Solicitação:

```curl
curl -X GET http://localhost:9002/api/v1/fact

```

#### Resposta:

``` json
[
    {
        "id": 1,
        "name": "fulano de tal",
        "idade": 19
    }
]
```