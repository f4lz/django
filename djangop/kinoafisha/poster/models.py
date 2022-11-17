from audioop import reverse
from distutils.command.upload import upload
from operator import truediv
from turtle import title
from django.db import models

class Poster(models.Model):
    title = models.CharField(max_length=255, verbose_name= "Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name= "Жанр")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото" )
    is_published = models.BooleanField(default=True, verbose_name= "Публикация")
    cat = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name="Категории")



    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.title

   
        

    class Meta:
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'
        ordering = ['title']
        

    

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
        



    