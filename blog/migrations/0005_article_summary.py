# Generated by Django 4.2.5 on 2023-11-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]