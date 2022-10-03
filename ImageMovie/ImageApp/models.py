from django.db import models

# Create your models here.
class TestModel(models.Model):
    files = models.ImageField('画像ファイル', null=True, blank=True, default='')

    def __str__(self):
        return f'{self.files}'

