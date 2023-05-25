from django.db import models

# Create your models here.


class Student(models.Model):
    std_id = models.AutoField(primary_key=True)
    std_name = models.CharField(max_length=15)
    std_email = models.EmailField(max_length=30)
    std_contact = models.IntegerField()

    class Meta:
        db_table = "student"