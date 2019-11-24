# pizza-ordering


## Run:
```sh
docker-compose up -d api
```

## Connect to container and run tests:
```sh
docker-compose exec api bash
```
then:
```sh
python manage.py test
```

## API:

### URL:
```sh
http://localhost:8000/api/v1/ordering/order/
```

Constants:
 - `status`: `1`(Ordered), `2`(In progress, not editable order), `3`(Delivered, not editable order)
 - `flavor`: `1`(Margarita), `2`(Marinara), `3`(Salami)
 - `size`: `1`(Small), `2`(Medium), `3`(Large)


#### Example GET data:
URL: `http://localhost:8000/api/v1/ordering/order/`
URL Detail: `http://localhost:8000/api/v1/ordering/order/1/`

```json
[
  {
    "id": 1,
    "customer": {
      "name": "Test",
      "address": "Test",
      "phone": "Test"
    },
    "pizza": [
      {
        "id": 1,
        "flavor": 2,
        "details": [
          {
            "id": 1,
            "size": 1,
            "quantity": 2
          }
        ]
      }
    ],
    "status": 1,
    "ordered_at": "2019-11-24T15:49:04"
  }
]
```

#### Example POST data:
URL: `http://localhost:8000/api/v1/ordering/order/`

```json
{
    "customer": {
      "name": "Test",
      "address": "Test",
      "phone": "Test"
    },
    "pizza": [
      {
        "flavor": 2,
        "details": [
          {
            "size": 1,
            "quantity": 2
          }
        ]
      }
    ],
    "status": 1
  }
```

#### Example PUT data:
URL: `http://localhost:8000/api/v1/ordering/order/1/`
```json
{
    "id": 1,
    "customer": {
      "name": "New name",
      "address": "New address",
      "phone": "New phone"
    },
    "pizza": [
      {
        "id": 1,
        "flavor": 2,
        "details": [
          {
            "id": 1,
            "size": 2,
            "quantity": 2
          }
        ]
      },
      {
        "flavor": 1,
        "details": [
          {
            "size": 2,
            "quantity": 1
          }
        ]
      }
    ],
    "status": 1,
    "ordered_at": "2019-11-24T15:49:04"
  }
```
