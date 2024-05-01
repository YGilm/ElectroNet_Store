from django.db import models

NULLABLE = {'null': True, 'blank': True}


class BusinessUnit(models.Model):
    """
    Представляет звено в цепочке поставок, который может быть заводом, розничной сетью
    или индивидуальным предпринимателем.
    """
    TYPE_CHOICES = (
        (0, 'Factory'),  # Завод
        (1, 'Retail'),  # Розничная сеть
        (2, 'Entrepreneur')  # Индивидуальный предприниматель
    )

    title = models.CharField(max_length=255, verbose_name='Название')
    email = models.EmailField(verbose_name='Электронная почта')

    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    unit_type = models.IntegerField(choices=TYPE_CHOICES, verbose_name='Тип учреждения')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бизнес-единица'
        verbose_name_plural = 'Бизнес-единицы'


class Product(models.Model):
    """
    Представляет продукт, произведенный или продаваемый бизнес-единицей в цепочке поставок.
    """
    product_name = models.CharField(max_length=255, verbose_name='Наименование')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выпуска')
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, verbose_name='Принадлежит учреждению',
                                      related_name='products')

    def __str__(self):
        return f"{self.product_name} {self.model}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
