from django.db import models

class UserModel(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length = 22)
    age = models.IntegerField()
    state_of_origin = models.CharField(max_length = 22)
    choice_of_candidate = models.CharField(max_length = 22)
    review = models.TextField(max_length=None)

    def __str__(self):
        return self.name


