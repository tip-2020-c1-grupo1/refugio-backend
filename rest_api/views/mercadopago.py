from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view()
def get_preference_id(request):
    amount = request.GET.get('amount', 0)
    data = amount
    """
    try :
        ml_request = requests.post(url='https://foo.com', data={'amount': amount}, verify=False)
        data = ml_request.text
    except :
        return Response({"error": 'Algo salio mal'}, status=status.HTTP_400_BAD_REQUEST)
    
    """
    return Response({"message": data})