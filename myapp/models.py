from django.db import models

class Persion(models.Model):
    __tablename__ = "myapp_persion"
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()