from django.db import models
from django_mysql.models import ListCharField, ListTextField

CHOICES =( 
    ("Active", "Active"), 
    ("Inactive", "Inactive"), 
) 


class Excursion(models.Model):
    name = models.CharField(max_length=22)
    detailPageName = models.CharField(max_length=33)
    portID = models.CharField(max_length=4)
    type = models.CharField(max_length=10)
    topology = ListTextField(base_field= models.IntegerField(blank=True), size=100)
    activityLevel = models.CharField(max_length=44)
    collectionType = models.CharField(max_length=22)
    duration = models.CharField(max_length=33)
    language = ListTextField(base_field= models.CharField(max_length=11, blank=True), size=100)
    priceLevel = models.IntegerField()
    currency = models.CharField(max_length=22)
    mealInfo = models.CharField(max_length=22)
    status = models.CharField(max_length=22, choices=CHOICES, default='Active')
    shortDescription = models.CharField(max_length=44)
    longDescription = models.CharField(max_length=88)
    externalContent = models.BooleanField(default=False)
    minimumAge = models.IntegerField()
    wheelChairAccessible = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    objects = models.Manager()

    class Meta:
        db_table = 'Excursions'
        ordering = ['name']
        verbose_name = 'Excursions'
        verbose_name_plural = 'Excursions'

    def __str__(self):
        return self.name
    














