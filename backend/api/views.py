from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer



@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """"
    DRF API View
    """
    data = request.data
    return Response (data)
