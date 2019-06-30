from django.db import models
from django.contrib.auth.models import User

# 튜터가 글을 쓸 때 가지는 속성(작성자, 타이틀, 내용, 작성시간, 이미지)
category = (('디자인', '디자인'), ('뷰티', '뷰티'), ('영상', '영상'), ('외국어', '외국어'), ('음악', '음악'),('스포츠', '스포츠'))
sub_category = (('포토샵', '포토샵'), ('일러스트레이터', '일러스트레이터'), ('메이크업', '메이크업'), 
    ('헤어', '헤어'), ('패션', '패션'), ('프리미어', '프리미어'), ('에프터이펙트', '에프터이펙트'), ('파이널컷', '파이널컷'), 
    ('영어', '영어'), ('중국어', '중국어'), ('일본어', '일본어'), ('불어', '불어'), ('독일어', '독일어'), ('보컬', '보컬'),
    ('피아노', '피아노'), ('성악', '성악'), ('바이올린', '바이올린'), ('플룻', '플룻'), ('빙구', '빙구'),
    ('족구', '족구'), ('축구', '축구'), ('테니스', '테니스'), ('스키', '스키'))
class TutorRequest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    tutor_category = models.CharField(max_length=10, choices=category, default='디자인')
    tutor_subcategory = models.CharField(max_length=10, choices=sub_category, default='포토샵')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

# 튜티가 글을 쓸 때 가지는 속성(작성자, 타이틀, 내용, 작성시간, 이미지)
class TutorApply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    tutor_category = models.CharField(max_length=10, choices=category, default='디자인')
    tutor_subcategory = models.CharField(max_length=10, choices=sub_category, default='포토샵')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title

# 튜터가 쓴 글에 댓글을 남기기 위한 모델.
class TutorComment(models.Model):
    blog = models.ForeignKey('TutorRequest',on_delete=models.CASCADE, related_name='tutorComments')
    comment_author = models.CharField(max_length = 10)
    comment_contents = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

# 튜티가 쓴 글에 댓글을 남기기 위한 모델.
class TuteeComment(models.Model):
    blog = models.ForeignKey('TutorApply',on_delete=models.CASCADE, related_name='tuteeComments')
    comment_author = models.CharField(max_length = 10)
    comment_contents = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
