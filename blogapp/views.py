from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import *
from . import aesEncrypt as aes
from . import randomCommentCreator as rc
import numpy as np


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

class CommentsView(generic.ListView):
	context_object_name = 'comments'

	def get_queryset(self):
		randomText = rc.random_generator(1000)
		frequencyOfAnalysis = rc.frequency_of_letters(randomText).most_common()
		standardDeviation = np.std(list(rc.frequency_of_letters(randomText).values()))
		randomComment = Comments.objects.create(randomText=randomText,
		frequencyOfAnalysis=frequencyOfAnalysis, standardDeviation=standardDeviation,
		published_date=timezone.now())
		randomComment.save()
		comments = Comments.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
		return comments








