from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import User


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

ESTADO = (
	('b', 'Borrador'),
	('p', 'Publicado'),
	)




class Snippet(models.Model):
	
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('created',)



class Category(models.Model):
	name = models.CharField(max_length = 100, db_index= True)

	def __unicode__(self):
		return self.name
	
	class Meta:
		ordering = ('name',)




class Post(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	category = models.ManyToManyField(Category)
	title = models.CharField(max_length = 200)
	body = models.TextField()
	status = models.CharField(max_length = 1, choices = ESTADO)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('author',)


class Comment(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	post = models.ForeignKey(Post, null = True)
	title = models.CharField(max_length = 200)
	body = models.TextField()
	
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('author',)	
	