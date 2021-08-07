#apeando

import requests
import json
#url="https://api.mercadolibre.com/users/test_user"
url="https://api.mercadolibre.com/items"


#token="APP_USR-4726037063911819-060217-da42f90bc23753428c2cced8a41b20c2-553279780"
token="APP_USR-4726037063911819-060217-e9f8dfc6ba5d7d92a52a870824956735-769330499"

#headers = {"Authorization": str("Bearer "+token),"Content-type": "application/json" }
headers = {"Authorization": str("Bearer "+token)}


data= {
  "title":"Libro losada - No Ofertar",
  "category_id":"MLA412445",
  "price":350,
  "currency_id":"ARS",
  "available_quantity":1,
  "buying_mode":"buy_it_now",
  "condition":"new",
  "listing_type_id":"gold_special",
  "description":{
     "plain_text":"Descripción con Texto Plano \n"
  },
  "sale_terms":[
     {
        "id":"WARRANTY_TYPE",
        "value_name":"Garantía del vendedor"
     },
     {
        "id":"WARRANTY_TIME",
        "value_name":"30 días"
     }
  ],
  "pictures":[
     {
        "source":"https://i.postimg.cc/sXfYNVzf/9509515850001.jpg"
     }
  ],
  "attributes":[
     {
        "id":"AUTHOR",
        "value_name":"Covadonga Perez Lozano"
     },
     {
        "id":"BOOK_GENRE",
        "value_name":"Suspenso"
     },
     {
        "id":"BOOK_TITLE",
        "value_name":"Aprendiendo a amar"
     },
     {
        "id":"FORMAT",
        "value_name":"Papel"
     },
     {
        "id":"GTIN",
        "value_name":"9789509580275"
     },
     {
        "id":"ITEM_CONDITION",
        "value_name":"Nuevo"
     },
     {
        "id":"LANGUAGE",
        "value_name":"Español"
     },
     {
        "id":"NARRATION_TYPE",
        "value_name":"Auto ayuda"
     },
     {
        "id":"PUBLISHER",
        "value_name":"Covadonga"
     },
     {
        "id":"SELLER_SKU",
        "value_name":"9789509580275"
     }
  ]
}
req = requests.post(url, headers=headers, json=data)

print(req)

print(req.content)