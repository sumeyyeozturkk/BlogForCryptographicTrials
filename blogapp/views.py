from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import *


class PostView(generic.ListView):
	template_name = 'post_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
