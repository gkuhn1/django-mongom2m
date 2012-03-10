from django.db import models
from fields import MongoDBManyToManyField
from django_mongodb_engine.contrib import MongoDBManager

class TestCategory(models.Model):
    objects = MongoDBManager()
    title = models.CharField(max_length=254)

class TestTag(models.Model):
    objects = MongoDBManager()
    name = models.CharField(max_length=254)

class TestArticle(models.Model):
    objects = MongoDBManager()
    main_category = models.ForeignKey(TestCategory, related_name='main_articles')
    categories = MongoDBManyToManyField(TestCategory)
    tags = MongoDBManyToManyField(TestTag, related_name='articles', embed=True)
    title = models.CharField(max_length=254)
    text = models.TextField()
    
    def __unicode__(self):
        return self.title
