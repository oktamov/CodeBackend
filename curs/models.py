from django.db import models


class BaseCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250, null=False, unique=False)
    slug = models.SlugField(max_length=255, null=False)
    basecategory = models.ForeignKey(BaseCategory, on_delete=models.CASCADE, related_name='basecategory')

    def __str__(self):
        return self.name


class Courses(models.Model):
    title = models.CharField(max_length=250, null=False, unique=True)
    paragraph = models.TextField()
    thumbnail = models.ImageField(upload_to='images/')
    description = models.TextField()
    Duration = models.CharField(max_length=250, null=True)
    teacher = models.CharField(max_length=250, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course')

    def __str__(self):
        return self.title


class LessonTopic(models.Model):
    name = models.CharField(max_length=250, null=False)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lessons(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    Duration = models.CharField(max_length=250, null=True)
    topic = models.ForeignKey(LessonTopic, models.CASCADE)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name
