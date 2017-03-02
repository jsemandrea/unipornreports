from django.db import models
from users.models import User

class CSV(models.Model):
    user = models.ForeignKey(User)
    uploaded_csv1 = models.FileField(upload_to = '.')
    uploaded_csv2 = models.FileField(upload_to = '.')
    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name = 'CSV'
        verbose_name_plural = 'CSVs'
        unique_together = ('uploaded_csv1', 'uploaded_csv2')

class Report(models.Model):
    is_active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    csvs = models.ManyToManyField(CSV, blank = True, null = True)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
