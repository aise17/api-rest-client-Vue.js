from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Post, Comment, Category
from django.contrib.auth.models import User, Group

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields =('id', 'title', 'code', 'linenos', 'language', 'style')

	def create(self, validated_data):
		"""
		Create and return a new `Snippet` instance, given the validated data.
		"""
		return Snippet.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Snippet` instance, given the validated data.
		"""
		instance.title = validated_data.get('title', instance.title)
		instance.code = validated_data.get('code', instance.code)
		instance.linenos = validated_data.get('linenos', instance.linenos)
		instance.language = validated_data.get('language', instance.language)
		instance.style = validated_data.get('style', instance.style)
		instance.save()
		return instance


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('author', 'category', 'title', 'body', 'status')

	def create(self, validated_data):
		return Post.objects.create(**validated_data)

	def update(self, validated_data):
		instance.author = validated_data.get('author', validated_data)
		instance.category= validated_data.get('category', validated_data)
		instance.title = validated_data.get('title', validated_data)
		instance.body = validated_data.get('body', validated_data)
		instance.status = validated_data.get('status',validated_data)
		instance.save()
		return instance



class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('author', 'post', 'title', 'body')

	def create(self, validated_data):
		return Comment.create(**validated_data)

	def update(self, validated_data):
		instance.author = validated_data.get('author', validated_data)
		instance.post= validated_data.get('post', validated_data)
		instance.title = validated_data.get('title', validated_data)
		instance.body = validated_data.get('body', validated_data)
		instance.save()
		return instance



class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('name')

	def create(self, validated_data):
		return Category.create(**validated_data)

	def update(self, validated_data):
		instance.name = validated_data.get('name', validated_data)
		instance.save()
		return instance		


class SingUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password')
		write_only_fields = ('password',)


