from django.shortcuts import render
from rest_framework.views   import APIView
from rest_framework.response    import Response
from rest_framework.exceptions  import NotFound
from .models    import Feed
from .serializers   import FeedSerializer

# Create your views here.
class Feeds(APIView):
    def get(self, request):
        feeds = Feed.objects.all() #객체
        # 객체 >> JSON (Serialize)
        serializer = FeedSerializer(feeds, many=True)

        return Response(serializer.data)
    #api/v1/feeds [POST]
    def post(self, request):
        # 역직렬화 클라이언트가 보내준 JSON >> object
        serializer = FeedSerializer(data = request.data)
        
        if serializer.is_valid():
            feed = serializer.save(user=request.user)
            serializer = FeedSerializer(feed)

            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        # feed(object) >> JSON 변경필요 : serializer
        serializer = FeedSerializer(feed)
        
        return Response(serializer.data)