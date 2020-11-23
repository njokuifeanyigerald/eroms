from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Entry(models.Model):       # this is a table called Entry
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add= True)  
    
        

    # def __str__(self):
    #     return 'Entry #{}'.format(self.id)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = 'entries'


class BMI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight =  models.FloatField()
    age = models.DateField()
    date_posted = models.DateTimeField(auto_now_add= True)


    def BMICalculation(self):
        return 703 * (self.weight/self.height**2)


