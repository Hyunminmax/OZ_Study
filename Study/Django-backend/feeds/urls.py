from django.urls    import path
from .          import views

urlpatterns = [
    path('', views.show_feed),
    path('<int:feed_id>/<str:feed_content>/', views.show_one_feed),
    path('all/', views.show_all_feed)
]