from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import *
from . import aesEncrypt as aes


class PostView(generic.ListView):
	template_name = 'post_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


class EncryptedPostView(generic.ListView):
	context_object_name = 'encryptedPosts'

	def get_queryset(self):
		encPost =EncryptedPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
		for i in range(0,len(encPost)):
			key = str(encPost[i].key)
			plainText = encPost[i].plainText
			encText = aes.encrypt_text(key,plainText)
			decText = aes.decrypt_text(key,encText)
			encPost[i].encryptedText = encText
			encPost[i].decryptedText = decText
			encPost[i].save()
		return encPost