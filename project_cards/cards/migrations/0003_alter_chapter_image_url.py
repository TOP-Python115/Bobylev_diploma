# Generated by Django 4.1.3 on 2022-12-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_chapter_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
