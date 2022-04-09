from django.db import models

class plans(models.Model):
    data=models.DateField()
    OSOBISTE='OS'
    PRACA='PR'
    grupy=[(OSOBISTE,'osobiste'),(PRACA,'praca')]

    grupa = models.CharField(
        max_length=2,
        choices=grupy,
        default=OSOBISTE,
    )
    
    