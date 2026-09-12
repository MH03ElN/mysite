from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	content = models.TextField()
	image = models.ImageField(upload_to='blog/', blank=True, null=True)
	is_published = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title
