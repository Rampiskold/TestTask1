from django.db import models


# Модель тегов
class Tags(models.Model):
    name_tag = models.CharField("Название тега", max_length=150, blank=False,
                                default="")
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_date = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name_tag


# Модель новостей
class News(models.Model):
    title = models.CharField("Название статьи", max_length=150, blank=False,
                             default=None)
    description = models.TextField("Описание темы", blank=False, default=None)
    tags = models.ForeignKey(Tags, blank=True, default=None,
                             on_delete=models.PROTECT, related_name='news')
    main = models.BooleanField('Главная статья', default=False)
    number_views = models.IntegerField('Кол-во просмотров', default=0)
    img = models.ImageField(upload_to="img_news", width_field=None,
                            height_field=None, blank=False)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_date = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
