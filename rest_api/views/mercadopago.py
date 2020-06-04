from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import urllib3

urllib3.disable_warnings()

BASE_URL = 'https://api.mercadopago.com/'

ACCESS_TOKEN = 'APP_USR-6231114851810274-052404-b435aba1bae759453a0cb5b6975e5bd8-573077291'

import mercadopago

mp = mercadopago.MP(ACCESS_TOKEN)

headers = {
    'content-type': 'application/json',
}

params = (
    ('access_token', ACCESS_TOKEN),
)



#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://api.mercadopago.com/checkout/preferences?access_token=ACCESS_TOKEN_ENV', headers=headers, data=data)


@api_view()
def get_preference_id_via_mp(request):
    amount = float(request.GET.get('amount', 1))
    preference = {
        "items": [
            {
                "title": "Donación Refug.io",
                "quantity": 1,
                "description": "Caridad",
                "currency_id": "ARS",
                "unit_price": 1.0
            }
        ]
    }

    reference = mp.create_preference(preference)
    print(reference)
    return Response({"message": reference})


@api_view()
def get_preference_id(request):
    amount = float(request.GET.get('amount', 0))
    preference_url = 'checkout/preferences?access_token=' + ACCESS_TOKEN
    data = {
        "items": [
            {
                "title": "Donación Refug.io",
                "description": "Caridad",
                "quantity": 1,
                "currency_id": "ARS",
                "unit_price": 1.0
            }
        ]
    }
    data2 = {
        "items": [
            {
                "title": "Donación Refug.io",
                "description": "Caridad",
                "quantity": 1,
                "currency_id": "ARS",
                "unit_price": amount
            }
        ],
        "back_urls": {
            "success": "http://localhost:3000/donación/exito",
            "pending": "http://localhost:3000/donación/pendiente",
            "failure": "http://localhost:3000/donación/fallo"
        }
    }
    try :
        ml_request = requests.post('https://api.mercadopago.com/checkout/preferences', headers=headers, params=params,
                                 data=data, verify=False)
        """"
        ml_request = requests.post(url=BASE_URL + preference_url,
                                   data=data,
                                   headers={
                                       'content-type': 'application/json'},
                                   verify=False)
        """
        print(ml_request.text)
        response_data = ml_request.content
        print(response_data)
        # podria haber un encoding de esto pero escribe y lo vemos
    except:
        return Response({"error": 'Algo salio mal'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": response_data})