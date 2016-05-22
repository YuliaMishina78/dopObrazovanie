from django.db import models


class Site(models.Model):
    Url = models.CharField(max_length=200, null=False, blank=False)
    Correl = models.FloatField(default=0, null=False, blank=False)


class Teacher(models.Model):
    Url = models.CharField(max_length=200, null=False, blank=False)
    Name = models.CharField(max_length=100, null=False, blank=False)
    Money = models.IntegerField(default=0, null=False, blank=False)
    Subjects = models.CharField(max_length=200, null=False, blank=False)
    Metro = models.CharField(max_length=1000, null=False, blank=False)
    ComeHome = models.CharField(max_length=50, null=False, blank=False)
    Status = models.CharField(max_length=50, null=False, blank=False)
    Feedback = models.IntegerField(default=0, null=False, blank=False)
    SkypeNames = models.BooleanField(default=False, null=False, blank=False)
    RatingSum = models.IntegerField(default=0, null=True, blank=True)
    Rating = models.IntegerField(default=0, null=False, blank=False)
    RatingDivSum = models.FloatField(default=0, null=False, blank=False)
    FeedDivSum = models.FloatField(default=0, null=False, blank=False)
    Funct = models.FloatField(default=0, null=False, blank=False)
    FromSite = models.ForeignKey(Site, null=False, blank=False, on_delete=models.CASCADE)


class Favorites(models.Model):
    FavoriteTeacher = models.ForeignKey(Teacher, null=False, blank=False, on_delete=models.CASCADE)
