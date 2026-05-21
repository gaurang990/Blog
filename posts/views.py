from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})
def post_detail(request,id):
    post= get_object_or_404(Post,id=id)
    return render(request,'post_detail.html',{'post':post})
def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form=PostForm()
    return render(request,'create_post.html',{'form':form})
def update_post(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':

        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PostForm(instance=post)

    return render(request, 'update_post.html', {'form': form})
def delete_post(request, id):

    post = get_object_or_404(Post, id=id)

    post.delete()

    return redirect('home')

@api_view(['GET', 'POST'])
def api_posts(request):

    # GET all posts
    if request.method == 'GET':

        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    # CREATE post
    elif request.method == 'POST':

        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
    
def api_post_detail(request, id):

    try:
        post = Post.objects.get(id=id)

    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET single post
    if request.method == 'GET':

        serializer = PostSerializer(post)

        return Response(serializer.data)

    # UPDATE post
    elif request.method == 'PUT':

        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE post
    elif request.method == 'DELETE':

        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)