# Generated by Django 4.0.6 on 2022-07-18 17:10

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'CATEGORY',
            },
        ),
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('comment', models.TextField()),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
                ('fk_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.category')),
            ],
            options={
                'db_table': 'SPENDING',
            },
        ),
    ]
