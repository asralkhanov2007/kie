from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
	name = models.CharField("Category name:", max_length=100)
	slug = models.SlugField("*", max_length=100, unique=True)
	class Meta:
		verbose_name_plural ='Kategoriyalar'
		ordering = ['-id']

	def __str__(self):
		return self.name

class Posts(models.Model):
	title = models.CharField('Post title:', max_length=200)
	slug = models.SlugField('Post slug:', max_length=100, unique=True)
	img =  models.ImageField(upload_to='post_img/', blank=True)
	body = RichTextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='categories')
	author = models.CharField('Post author:', max_length=80)
	published = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural ='Hamma postlar'
		ordering = ['-published']

	def __str__(self):
		return self.title

class Contact(models.Model):
	name = models.CharField('Ismi', max_length=50)
	surname = models.CharField('Familyasi', max_length=50)
	phone = models.CharField('Telefon raqami', max_length=250)
	message = models.TextField('Xabari',)

	class  Meta:
		verbose_name = 'Aloqa'
		verbose_name_plural = 'Aloqalar'

	def __str__(self):
		return f"{self.name}"
class Ordering(models.Model):
	# title = models.ForeignKey(Posts, verbose_name='Nomlar', on_delete=models.CASCADE)
	title = models.CharField('Ordered posts',max_length=250)
	# title = models.ManyToManyField(Posts,verbose_name='nomlar',related_name='titles')

	class Meta:
		verbose_name = 'Zakaz'
		verbose_name_plural = 'Zakazlar'
	
	def __str__(self):
		return f"{self.title}"