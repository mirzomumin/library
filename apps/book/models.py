from django.db import models

from helpers.models import BaseModel


# Create your models here.


class Category(BaseModel):
    '''Category of book'''
    name = models.CharField(max_length=256, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        '''Representation of Category model'''
        return self.name


class Author(BaseModel):
    '''Author of book'''
    name = models.CharField(max_length=256, db_index=True,
                            unique=True)

    def __str__(self):
        '''Representation of Author model'''
        return self.name


class Book(BaseModel):
    '''Simple book model'''
    name = models.CharField(max_length=256, db_index=True,
                            unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Relations
    categories = models.ManyToManyField(Category,
                                        related_name='books')
    authors = models.ManyToManyField(Author, db_index=True,
                                     related_name='books')

    def __str__(self):
        '''Representation of Book model'''
        return self.name
