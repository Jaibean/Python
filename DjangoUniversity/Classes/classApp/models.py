from django.db import models


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, blank=False)
    CourseNumber = models.IntegerField(blank=False)
    InstructorName = models.CharField(max_length=100, blank=False)
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.Title
