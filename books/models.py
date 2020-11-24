from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Book(models.Model):
    title = models.CharField("Название", max_length=100, blank=False)
    file = models.FileField(blank=False, upload_to="all_books/")
    photo = models.ImageField("Обложка", upload_to="image/", blank=False)
    description = models.TextField("Описание", blank=False)
    author = models.CharField(max_length=150, blank=False)
    page = models.IntegerField("Страницы", blank=False)
    isbn = models.SmallIntegerField("ISBN", blank=False, unique=True)
    publisher = models.CharField("Издатель", max_length=250)
    year = models.DateField("Год",blank=False)
    lanquages = models.CharField("Язык", max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    country = models.CharField("Страна", max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"

