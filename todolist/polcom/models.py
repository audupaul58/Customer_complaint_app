from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Polcom(models.Model):
    
    MYCHOICE = (
        ("pending", "PENDING"),
        ("done", "DONE")
    )
    
    PRINCIPAL = (
         ("yes", "YES"),
        ("no", "NO")
        
    )
    
    phone_number = models.CharField(max_length=11)
    names = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    alternate_num = models.CharField(max_length=11)
    status = models.CharField(choices=MYCHOICE, max_length=7)
    principal = models.CharField(choices=PRINCIPAL, max_length=3)
    rank = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.phone_number
    
    class Meta:
        ordering = ('-created_at', )
    
