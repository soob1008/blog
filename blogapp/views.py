from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here
# 글 목록 보기
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'board/post_list.html', {'posts': posts})

# 글 상세 보기
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'board/post_detail.html', {'post': post})

# 글 작성
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'board/post_form.html', {'form': form})

# 글 수정
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'board/post_form.html', {'form': form})


# 글 삭제
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'board/post_confirm_delete.html', {'post': post})