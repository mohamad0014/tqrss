from django.db import models


class Plan(models.Model):
    plan_name = models.CharField(max_length=50)
    associates = models.IntegerField()
    shift_length = models.IntegerField()
    time_units = (
        ('S', 'Second'),
        ('M', 'Minute'),
    )
    start_date = models.DateField()
    horizon = models.IntegerField()
    statuses = (
        ('D', 'Draft'),
        ('R', 'Released'),
    )
    create_time = models.DateTimeField()
