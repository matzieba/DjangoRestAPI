
from rest_framework.response import Response
from rest_framework.decorators import api_view


from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():

        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"not god data"}, status = 400)
