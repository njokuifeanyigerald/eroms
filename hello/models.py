from django.db import models


# Create your models here.

class Entry(models.Model):       # this is a table called Entry
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)     #automaticaly set the date
        

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'

