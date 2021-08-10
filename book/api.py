from rest_framework.response import Response
from .models import book
from .serializers import BookSerializers
from rest_framework.decorators import api_view

@api_view(['GET'])
def bookListApi(request):
    all_books=book.objects.all()
    data =BookSerializers(all_books,many=True).data
    return Response({'data':data})
