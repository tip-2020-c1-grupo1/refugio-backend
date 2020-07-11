import json
from json.encoder import JSONEncoder

import requests
import urllib3
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

urllib3.disable_warnings()

BASE_URL = 'https://api.mercadopago.com/'

ACCESS_TOKEN = 'APP_USR-6231114851810274-052404-b435aba1bae759453a0cb5b6975e5bd8-573077291'


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
                "unit_price": amount
            }
        ],
        "back_urls": getattr(settings, 'MP_URLS', None)

    }
    try:
        ml_request = requests.post('https://api.mercadopago.com/' + preference_url, data=JSONEncoder().encode(data))
        print(ml_request.text)
        response_data_string = ml_request.content.decode('utf-8')
        print(response_data_string)
        response_data_json = json.loads(response_data_string)
        print(response_data_json)
        # podria haber un encoding de esto pero escribe y lo vemos
    except:
        return Response({"error": 'Algo salió mal'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(response_data_json['init_point'])
