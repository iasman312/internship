from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,
                            verbose_name="Название товара")
    description = models.TextField(max_length=2000, null=True, blank=True,
                                   verbose_name="Описание товара")
    category = models.ForeignKey('shop.Category', related_name='products',
                                 verbose_name='Статус',
                                 on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=7, decimal_places=2,
                                verbose_name="Стоимость")

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.id}. {self.name}: {self.description}'


class Category(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False,
                            verbose_name='Название')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'