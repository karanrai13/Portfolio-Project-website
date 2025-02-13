from django.db import models

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from '+self.name +' - '+ self.email 

class Image(models.Model):
    image=models.ImageField(upload_to='myimage')
    timeStamp = models.DateTimeField(blank=True)

    