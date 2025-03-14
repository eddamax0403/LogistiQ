from django.db import models

# Create your models here.

class Zip(models.Model):
    zip_code = models.IntegerField()

    def __str__(self):
        return str(self.zip_code)



