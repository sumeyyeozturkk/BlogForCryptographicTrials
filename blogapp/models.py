from django.db import models
from django.utils import timezone 

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class EncryptedPost(models.Model):
    title = models.CharField(max_length=200)
    plainText = models.TextField()
    encryptedText= models.TextField(null=True)
    decryptedText = models.TextField(null=True)
    key = models.CharField(max_length=200,null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)

