from django.db import models


class school(models.Model):
    Poniedzialek=models.CharField(
        max_length=11,
        default='07:00-15:40'
    )
    Wtorek=models.CharField(
        max_length=11,
        default='07:00-15:40'
    )
    Sroda=models.CharField(
        max_length=11,
        default='07:00-15:40'
    )
    Czwartek=models.CharField(
        max_length=11,
        default='07:00-15:40'
    )
    Piatek=models.CharField(
        max_length=11,
        default='07:00-15:40'
    )
    Sobota=models.CharField(
        max_length=11,
        default='07:00-15:40'
    )

