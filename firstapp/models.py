from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100, db_index=True)


class MutipleColumnIndex(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        indexes = [
            models.Index(fields=['first_name', 'last_name'])
        ]

