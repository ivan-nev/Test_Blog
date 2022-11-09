from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


def post_list(request):
    # posts = Post.objects.filter(publisher_data__lte=timezone.now()).order_by('publisher_data')
    posts = Post.objects.order_by('publisher_data').all()
    Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/post_list.html', context=context)

def post_detail(reqest, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(reqest,'blog/post_detail.html', context=context)


# Create your views here.
