from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    is_active = models.BooleanField(verbose_name='активна', default=True, db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(max_length=128, verbose_name='название')
    image = models.ImageField(upload_to='product_images', blank=True, verbose_name='картинка')
    short_desc = models.CharField(max_length=120, verbose_name='краткое описание')
    description = models.TextField(verbose_name='описание', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='цена')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='количество на складе')
    is_active = models.BooleanField(verbose_name='активна', default=True, db_index=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('category', 'name')
