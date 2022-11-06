from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(publisher_data__lte=timezone.now()).order_by('publisher_data')
    context = {'posts':posts}
    return render(request, 'blog/post_list.html', context=context)

# Create your views here.
