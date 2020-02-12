from rest_auth.views import LoginView
from django.urls import path
from .api import PostList, post_like, profile_follow, ProfileList, PostImagesList

urlpatterns = [
    #AUTH URLS
    path('api/login', LoginView.as_view()),

    #POST URLS
    path('api/posts', PostList.as_view()),
    path('api/post/like/<post_id>', post_like),
    path('api/posts/images/<profile_id>', PostImagesList.as_view()),

    #PROFILE URLS
    path('api/profiles', ProfileList.as_view()),
    path('api/profiles/follow/<profile_id>', profile_follow),
    path('api/profiles/unfollow/<profile_id>', profile_follow, {'follow':False}),

]