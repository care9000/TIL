from django.shortcuts import render, get_object_or_404
from .models import Music, Artist, Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    # musics(queryset)->json 형태로 변환
    # many=True 는 하나의 옵션이아니라 여러가지이므로 씀
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

#뮤직의 세부정보 보여주기(404에러도 같이 가져옴)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerializer(music) # many=True옵션없음 하나의 객체이기때문에
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['POST'])
def comments_create(request, music_pk):
    # request.data -> 사용자가 HTTP body에 담아 날린 댓글(content) 내용
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
    return Response(serializer.data)
    
@api_view(['PUT','DELETE'])
def comments_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    #PUT
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Comment has been updated!!'})
    #DELETE
    else:
        comment.delete()
        return Response({'message': 'Comment has been deleted!!'})
