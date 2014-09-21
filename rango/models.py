from django.db import models

# Create your models here.
class UserPersonal(models.Model):
  name = models.CharField(max_length=128, unique=True)
  age = models.IntegerField(default=0)

  def __unicode__(self):
    return self.name + str(self.age)

class UserFinancial(models.Model):
  username = models.ForeignKey(UserPersonal)
  salary = models.IntegerField(default=0)
  otherIncome = models.IntegerField(default=0)

  def __unicode__(self):
    return str(self.salary)

