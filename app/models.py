from django.db import models


class Member(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    # Consider not storing plaintext passwords!
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.fname} {self.lname}"
