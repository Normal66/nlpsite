from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


#class Test
#    body = RichTextUploadingField(verbose_name='Code', null=True, blank=True)
#    comment = RichTextField(verbose_name='Comment Code')


class MenuManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(cansw=True)


class m_SprMenu(models.Model):  # Меню - Название, Иконка, Ссылка, Порядок
    object = MenuManager()
    title = models.CharField(max_length=15, verbose_name='Пункт меню')
    icons = models.ImageField(upload_to='menu/img/', blank=True, verbose_name='Иконка')
    links = models.URLField(verbose_name='Ссылка')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')
    cansw = models.BooleanField(default=True, verbose_name='Отображать')

    class Meta:
        ordering = ['order']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title
# -------------------------------------------------------------------------------------------------- #


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(cansw=True)


class m_Category(models.Model):
#    object = CategoryManager()
    published = CategoryManager()
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d', blank=True)
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')
    cansw = models.BooleanField(default=True, verbose_name='Отображать')

    class Meta:
        ordering = ['order']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category', args=[self.slug])
# -------------------------------------------------------------------------------------------------- #


class TreningManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(cansw=True)


class m_Trening(models.Model):
#    object = TreningManager()
    published = TreningManager()
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(m_Category, on_delete=models.CASCADE, related_name='trenings')
    image = models.ImageField(upload_to='program/%Y/%m/%d', blank=True, verbose_name='Картинка')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')
    cansw = models.BooleanField(default=True, verbose_name='Отображать')
    body = RichTextUploadingField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Тренинг'
        verbose_name_plural = 'Тренинги'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])
# -------------------------------------------------------------------------------------------------- #
