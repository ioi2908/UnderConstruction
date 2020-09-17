from django.db import models

class EmailNotify(models.Model):
    email = models.EmailField()
    comment = models.TextField(default='Tuma maoni..')
    
    def __str__(self):
        return self.email
