from snippets.models import Snippet ,Post, Comment, Category, User
from snippets.serializers import SnippetSerializer, PostSerializer, CommentSerializer, CategorySerializer, SingUpSerializer
from rest_framework import generics 
from permissions import IsAuthenticatedOrCreated




class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	ermission_classes = (IsAuthenticatedOrCreated,)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (IsAuthenticatedOrCreated,)


class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsAuthenticatedOrCreated,)


class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = (IsAuthenticatedOrCreated,)


class CategoryList(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = (IsAuthenticatedOrCreated,)

class SingUp(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = SingUpSerializer

