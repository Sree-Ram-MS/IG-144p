from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bio(models.Model):
    dob=models.DateField()
    options=(
        ("Male","Male"),
        ("Female","Female"),
        ("other","other")
    )
    gender=models.CharField(max_length=100,choices=options,default="Male")
    phone=models.IntegerField()
    status=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="User_profile_pic",null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Bio_user")

class Posts(models.Model):
    Image=models.ImageField(upload_to="post_img",null=True)
    caption=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_user")
    likes=models.ManyToManyField(User,related_name="liked_user")

    @property
    def allikes(self):
        return self.likes
    
    def likeduser(self):
        lk=self.likes.all()
        users=[u.username for u in lk]
        return users

class Comments(models.Model):
    comment=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment_user")
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="commented_post")
    