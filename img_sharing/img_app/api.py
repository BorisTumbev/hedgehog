from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Count
from .models import Post, Profile
from .serializers import PostSerializer, ProfileSerializer, PostImageSerializer


'''POST VIEWS'''

class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    serializer_class = PostSerializer
    queryset = Post.objects.annotate(l_count=Count('likes')).order_by('-l_count')

class PostImagesList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PostImageSerializer

    def get_queryset(self):
        curr_user = Profile.objects.get(id=self.kwargs.get('profile_id'))
        logged_user = self.request.user

        list_of_followers = list(curr_user.followers.all().values_list('id', flat=True))

        # checks if you have access to the images
        if logged_user == curr_user or logged_user.id in list_of_followers:
            return Post.objects.filter(author=curr_user).order_by('-created')
        else:
            return Post.objects.none()



@permission_classes((permissions.IsAuthenticated,))
@api_view(["POST"])
def post_like(request, post_id):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return JsonResponse({'error': 'no such post'}, safe=False)

    post.likes.add(request.user)

    return JsonResponse({'done': 'like is added'}, safe=False)

'''PROFILE VIEWS'''

class ProfileList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated, ]

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

@api_view(["POST"])
@permission_classes((permissions.IsAuthenticated,))
def profile_follow(request, profile_id, follow=True):

    try:
        user_to = Profile.objects.get(id=profile_id)
    except:
        return JsonResponse({'error': 'no such profile'}, safe=False)

    if follow:
        request.user.follows.add(user_to)
    else:
        request.user.follows.remove(user_to)

    return JsonResponse({'done': 'user is followed/unfollowed'}, safe=False)
