from django.urls import path
from .views import *

urlpatterns = [
    path('', PostView.as_view()),
    path('EncPosts', EncryptedPostView.as_view(), name = 'EncPost')
]