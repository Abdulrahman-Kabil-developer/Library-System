# Generated by Django 3.2.5 on 2021-07-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_rename_statu_book_borowingstatu'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
