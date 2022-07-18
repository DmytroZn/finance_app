from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Category(models.Model):
    name_category = models.CharField(max_length=50)
    date_time_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_category

    class Meta:
        db_table = "Category".upper()


class Spending(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.00'))])
    # amount = models.DecimalField(decimal_places=2, max_digits=12)
    comment = models.TextField(blank=True)
    date_time_created = models.DateTimeField(auto_now_add=True)
    fk_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)

    class Meta:
        db_table = "Spending".upper()
        ordering = ("-date_time_created",)



