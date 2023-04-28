from django.db import models


def image_upload_path(instance, filename):
    return f"images/{filename}"
    

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    condition = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        related_query_name='products'
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.category}"

class Attachment(models.Model):
    file = models.ImageField(upload_to=image_upload_path)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        related_query_name='images'
    )

    