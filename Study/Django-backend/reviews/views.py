from django.shortcuts import render
from .models    import Review
from .serializers   import  ReivewSerializer
from rest_framework.response    import Response
from rest_framework.views       import APIView
from rest_framework.exceptions  import NotFound

# Create your views here.
# api/v1/reviews [GET]
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReivewSerializer(reviews, many = True)

        return Response(serializer.data)
        

# api/v1/reviews/review_id [GET]
class reviewDetail(APIView):
    def get(self, request, review_id):
        try:
            review = Review.objects.get(id = review_id)
        except:
            raise NotFound

        serializer = ReivewSerializer(review)

        return Response(serializer.data)
