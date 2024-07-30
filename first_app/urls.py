from django.urls import path
from first_app import views
urlpatterns = [
    # path('',views.first1),#here the control is accessed
    path('',views.show_tweets, name='show_tweets'),
    path('home',views.home, name='home'),
    path('addTweet/',views.addTweet, name='addTweet'),
    path('<int:id>/edit/',views.edit_tweet, name='edit_tweet'),
    path('<int:id>/delete/',views.delete_tweet, name='delete_tweet'),
    path('registration/',views.registration, name='registration'),




]