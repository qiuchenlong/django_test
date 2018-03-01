from django.db import models

# Create your models here.

from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Person(models.Model):

    class Meta:
        db_table = 'tb_person'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    p_money = models.DecimalField(default=0, max_digits=19, decimal_places=10)
    p_age = models.IntegerField(default=0)

    def speak(self):
        return "The %s says %s" % (self.first_name, self.last_name)


# class User(models.Model):
#     class Meta:
#         db_table = 'tb_user'
#
#     u_id = models.IntegerField(primary_key=True)
#     username = models.CharField(max_length=64)
#     email = models.CharField(max_length=64)
#     phone = models.CharField(max_length=64)
#
#
# class Project(models.Model):
#     class Meta:
#         db_table = 'tb_project'
#
#     p_id = models.CharField(max_length=128, primary_key=True)
#     p_content = models.TextField()
#     p_parentid = models.CharField(max_length=128)
#     p_priority = models.IntegerField()
#     # p_note = models.CharField(max_length=128)
