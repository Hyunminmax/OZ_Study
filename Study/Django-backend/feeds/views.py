from django.shortcuts   import render
from django.http        import HttpResponse

# Create your views here.
def show_feed(request):
    return HttpResponse("show feed")

def show_one_feed(request, feed_id, feed_content):
    return HttpResponse(f"show one_feed. feed_id:{feed_id}, feed_content:{feed_content} ")

def show_all_feed(request):
    return HttpResponse("show all_feed")