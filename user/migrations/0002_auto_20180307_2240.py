# Generated by Django 2.0.2 on 2018-03-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
