from django.db import models
from django.conf import settings


class Diagnose(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    medication = models.TextField()
    image = models.FileField(upload_to='images/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return 'Question by {}'.format(self.user)


class SendMail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=250)
    body = models.TextField()


class Common(models.Model):
    name = models.CharField(max_length=250)
    symptom_desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    medication = models.TextField()

    def __str__(self):
        return self.name




