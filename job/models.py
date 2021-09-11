from django.db import models

# Create your models here.
'''
Django Model Fields
1- HTML Widgets
2- Validation
3- DB Size
'''
Job_Type = (
    ('Full time', 'Full time'),
    ('Part time', 'Patr time'),

)


class Job(models.Model):  # Table
    title = models.CharField(max_length=100)  # column
    job_type = models.CharField(max_length=15, choices=Job_Type)
    Description = models.TextField(max_length=1000)
    Published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    Experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
