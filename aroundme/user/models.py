from django.db import models
from django.contrib.auth.models import User

class Bio(models.Model):
    dob=models.DateField()
    options=(
        ("Male","Male"),
        ("Female","Female"),("Others","Others"),
    )
    gender=models.CharField(max_length=100,choices=options,default="Female")
    phone=models.IntegerField()
    status=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="user",null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Bio_user")

class Posts(models.Model):
    image=models.ImageField(upload_to="posted_images",null=True)
    caption=models.CharField(max_length=100)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="p_user")
    likes=models.ManyToManyField(User,related_name="liked_user")

    @property
    def cntlikes(self):
        return self.likes
    @property
    def likedusers(self):
        lk=self.likes.all()
        users=[u.first_name for u in lk]
        return users
    
class Comments(models.Model):
    comment=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="commented_user")
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="commented_post")






