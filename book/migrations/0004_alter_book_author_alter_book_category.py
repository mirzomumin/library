# Generated by Django 4.1.5 on 2023-01-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(db_index=True, related_name='books', to='book.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='books', to='book.category'),
        ),
    ]
