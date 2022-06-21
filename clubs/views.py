from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from clubs.models import Club
from clubs.serializers import ClubSerializer


@api_view(['GET'])
def club_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        if request.GET:
            snippets = Club.objects.filter(price__gte=request.GET.get("from_price"),
                                           price__lte=request.GET.get("to_price"))
        else:
            snippets = Club.objects.all()
        serializer = ClubSerializer(snippets, many=True)
        return Response(serializer.data)
