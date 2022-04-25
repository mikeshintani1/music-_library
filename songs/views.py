from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .models import Song
from .serializers import SongSerializer
from songs import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def music(request):
    songs = Song.objects.all()
    song_types_param = request.queery_params.get('title')
    sort_param = request.query_params.get('sort')
    custom_response_dictionary = {}
    if song_types_param:
        songs = songs.filter(song_type__type = song_types_param)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif sort_param:
        songs = songs.order_by(sort_param)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
