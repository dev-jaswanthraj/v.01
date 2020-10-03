from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from posts.models import Post
from .serializers import PostSerializer
from rest_framework import permissions

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_post_detail(request, id):

    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)