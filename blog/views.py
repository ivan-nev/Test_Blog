
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect




def post_list(request):
    # posts = Post.objects.filter(publisher_data__lte=timezone.now()).order_by('publisher_data')
    posts = Post.objects.order_by('publisher_data').all()
    Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/post_list.html', context=context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request,'blog/post_detail.html', context=context)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publisher_data = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request,'blog/post_edit.html', context=context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publisher_data = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})




# Create your views here.
