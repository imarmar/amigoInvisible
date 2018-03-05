from django.db import models
from django.contrib.auth.models import User

class Participant(models.Model):    
    """ 
        Name: (string) mandatory
        Email: (string) mandatory
        partner: ForeignKey Participant 
        user: ForeignKey to AdminUser
    """           
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    partner = models.CharField(max_length=100)
    user = models.ForeignKey(User)