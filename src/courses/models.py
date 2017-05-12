from __future__ import unicode_literals
from django.db import models


class Course(models.Model): 
    course_id = models.CharField(max_length=120)
    course_name = models.CharField(max_length=120)
    pre_req = models.CharField(max_length=120)
    quarter_ava = models.CharField(max_length=120)


    #updated = models.DateTimeField(auto_now=True, auto_now_add=False)
   # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __unicode__(self):
        return self.course_name

    def __str__(self):
        return self.course_name

# Create your models here.
# class ProjectRouter(object): 
#     def db_for_read(self, model, **hints):
#         "Point all operations on chinook models to 'chinookdb'"
#         if model._meta.app_label == 'projectdb':
#             return 'projectdb'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         "Point all operations on chinook models to 'chinookdb'"
#         if model._meta.app_label == 'projectdb':
#             return 'projectdb'
#         return 'default'
    
#     def allow_relation(self, obj1, obj2, **hints):
#         "Allow any relation if a both models in chinook app"
#         if obj1._meta.app_label == 'projectdb' and obj2._meta.app_label == 'projectdb':
#             return True
#         # Allow if neither is chinook app
#         elif 'projectdb' not in [obj1._meta.app_label, obj2._meta.app_label]: 
#             return True
#         return False
    
#     def allow_migrate(self, db, model):
#         if db == 'projectdb' or model._meta.app_label == "projectdb":
#             return False # we're not using syncdb on our legacy database
#         else: # but all other models/databases are fine
#             return True