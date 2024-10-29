from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length =200)
    price=models.IntegerField()
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Log(models.Model):
    LOG_TYPES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]
    log_type = models.CharField(max_length=10, choices=LOG_TYPES)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
  