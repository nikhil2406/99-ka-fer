from django.db import models

# Create your models here.
class UserPersonal(models.Model):
  name = models.CharField(max_length=128, unique=True)
  age = models.IntegerField(default=0)
  phone = models.CharField(max_length=10, unique=True)

  def __unicode__(self):
    return self.name + str(self.age) + self.phone

class UserFinancial(models.Model):
  userpersonal = models.ForeignKey(UserPersonal)
  salary = models.IntegerField(default=0)
  otherIncome = models.IntegerField(default=0)

  def __unicode__(self):
    return str(self.salary)

