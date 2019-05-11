from django.db import models

# Create your models here.

class Posts(models.Model): 
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(max_length=50, null=False, blank=False)
	text = models.TextField(null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_date']
		verbose_name = 'Publicação'
		verbose_name_plural = 'Publicações'

	def __str__(self):
		return self.title 