from django.db import models
import uuid
# Create your models here.
#signup model
class signup_model(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=255)
    details=models.TextField()
    chech1=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
       return str(self.username)

#session token
class SessionToken(models.Model):
    user = models.ForeignKey(signup_model,on_delete=models.PROTECT)
    session_token = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)



    def create_token(self):
        self.session_token = uuid.uuid4()

    def __str__(self):
        return str(self.user)
