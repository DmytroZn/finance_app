# Generated by Django 4.0.6 on 2022-07-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
