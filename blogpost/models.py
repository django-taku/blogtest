from django.db import models

# モデルの名前はクラスで定義する
# モデル　データーベス設計図
class SampeModel(models.Model):
    titel = models.CharField(max_length = 100) # 文字列型
    number = models.IntegerField() # 整数型

CATEGORY = (('business', 'ビジネス'), ('life','生活'), ('other','その他'))
class BlogModel(models.Model):# モデルの定義はクラスで定義する
    title = models.CharField(max_length = 100) # ブログのタイトル定義
    content = models.TextField()               # テキスト本文の定義
    postdate = models.DateField(auto_now_add = True) #日付の定義（日付を自動的に記録する）
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY # プルダウン定義
    )
    
    def __str__(self):
        return self.title
        
# Create your models here.
