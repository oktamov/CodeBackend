from django.contrib import admin
from .models import *

admin.site.register(BaseCategory)
admin.site.register(Category)
admin.site.register(Courses)
admin.site.register(LessonTopic)
admin.site.register(Lessons)
