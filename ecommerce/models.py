from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.PositiveBigIntegerField()
    description = models.TextField(default="This is the product's default description")
    quantity_in_stock = models.PositiveIntegerField(null=False, default=0)
    rating = models.PositiveIntegerField(default=5, validators=[MaxValueValidator(5)])
    image = models.TextField()
    slug = models.SlugField(unique=True, max_length=255, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
            'image': self.image,
            'quantity_in_stock': self.quantity_in_stock,
            'description': self.description,
            'slug': self.slug
        }
