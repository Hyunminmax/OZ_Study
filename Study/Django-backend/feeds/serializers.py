from rest_framework.serializers import ModelSerializer
from .models        import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReivewSerializer

class FeedSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only = True)
    review_set = ReivewSerializer(read_only = True, many = True)

    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1