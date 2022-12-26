from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Agricom(models.Model):
    
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
    status = models.CharField(max_length=7, choices=MYCHOICE)
    principal = models.CharField(max_length=3, choices=PRINCIPAL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.phone_number
    
    class Meta:
        ordering = ('-created_at', )
    
