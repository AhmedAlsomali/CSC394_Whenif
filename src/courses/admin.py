# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from courses.models import Course

class CourseAdmin(admin.ModelAdmin):
	list_display = ["course_id","course_name","pre_req", "quarter_ava"]
	list_display_links = ["course_id"]
	list_filter = ["course_id"]
	search_fields = [" course_id", " course_name"]
	class Metha:
		model = Course

admin.site.register(Course, CourseAdmin) 
