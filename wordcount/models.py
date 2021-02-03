from django.db import models

# Create your models here.


class FrequentWords(models.Model):
    word_url = models.URLField("URL", "URL", null=True)
    word_1 = models.CharField(max_length=20, null=True)
    word_2 = models.CharField(max_length=20, null=True)
    word_3 = models.CharField(max_length=20, null=True)
    word_4 = models.CharField(max_length=20, null=True)
    word_5 = models.CharField(max_length=20, null=True)
    word_6 = models.CharField(max_length=20, null=True)
    word_7 = models.CharField(max_length=20, null=True)
    word_8 = models.CharField(max_length=20, null=True)
    word_9 = models.CharField(max_length=20, null=True)
    word_10 = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.URL} | {self.word_1}"


