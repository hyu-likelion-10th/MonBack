from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

# Create your views here.
def home(request):
    # posts = Blog.objects.all()
    # 그냥 date는 오름차순
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts': posts})

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if request.method == 'POST':
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# django form을 이용해서 입력값을 받는 함수
# GET 요청(입력 값을 받을 수 있는 html 갖다 주기)과 POST 요청(입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리) 둘 다 처리 가능
def formcreate(request):
    # 입력한 내용을 DB에 저장
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다주기
        form = BlogForm()
    return render(request, 'form_create.html', {'form': form})

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다주기
        form = BlogForm()
    return render(request, 'form_create.html', {'form': form})    

def detail(request, blog_id):
    # blog_id 번째 글을 db로부터 갖고 와서
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # detail.html로 띄워주는 코드

    comment_form = CommentForm()

    return render(request, 'detail.html', {'blog_detail': blog_detail, 'comment_form': comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        # filled_form을 아직은 저장하지 말고 대기해
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id)

