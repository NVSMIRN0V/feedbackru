import transliterate
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# МОДЕЛЬ КАТЕГОРИИ
class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, editable=False, unique=True, db_index=True, verbose_name='url')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = transliterate.slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('fb-category', kwargs={'category_pk': self.pk})


# МОДЕЛЬ ОТЗЫВА
class Feedback(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема')
    author = models.ForeignKey(User, max_length=80, verbose_name='Автор', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Текст')
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, editable=False, unique=True, db_index=True, verbose_name='url')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['category']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = transliterate.slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('fb-detail', kwargs={'fb_slug': self.slug})
