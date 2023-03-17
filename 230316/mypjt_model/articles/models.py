from django.db import models

# Create your models here.
# django에서 다루고자 하는 데이터를 정의
# 게시글 정보를 DB에 저장
# 일단은 제목과 내용만 저장
# 모델을 만들건데... ORM 관련 동작을 해야 합니다.
# ORM 기능은 누가 만들어 놓은거 재사용 >> 상속
# Model 클래스를 상속하자. models 모듈에 구현되어 있음
class Article(models.Model):
    # 속성 = 이 속성이 DB에 어떤 형태로 저장될지 결정
    title = models.CharField(max_length=20) # CharField : 짧은 글
    content = models.TextField()    # TextField : 좀더 긴 글
