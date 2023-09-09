from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,
                            unique=True)
    sub_category = models.ForeignKey('self',
                                     on_delete=models.CASCADE,
                                     related_name='scategory',
                                     null=True, blank=True)
    is_sub = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:category_filter', args=[self.slug])


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=200, unique=True)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug])
