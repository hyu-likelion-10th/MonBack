from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시물에 달려있는 댓글인지를 알 수 있도록.
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
    

