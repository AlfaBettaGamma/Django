import datetime
from django.db import models

from django.utils import timezone

class Article(models.Model):
	article_titel = models.CharField('Название статьи', max_length = 200)
	article_text = models.TextField('Текст статьи')
	pub_date = models.DateTimeField('Дата публикации')

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

	def __str__(self):
		return self.article_titel

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('Имя автора', max_length = 50)
	comment_text = models.CharField('Текст комментария', max_length = 100)

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

	def __str__(self):
		return self.author_name