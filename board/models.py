from django.db import models
from user.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE: 유저 탈퇴 시 게시글 삭제 옵션 | SET_NULL, null=True: 유저 탈퇴해도 게시글은 유지(작성자는 알수 없게 됨.)
    title = models.CharField(max_length=100)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True) # auto_now_add: 게시글이 최초로 업로드된 시간을 저장하겠다는 의미
    img_url = models.URLField(null=True)

    class Meta:
        # 만약 테이블 이름을 지정하지 않으면 app이름_Model이름 으로 테이블이 작성됨(Ex. board_post)
        db_table="post"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="comment"