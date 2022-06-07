from django.db import models

class Plans(models.Model):

    zadanie=models.CharField(
        default="",
        max_length=20,
    )

    data=models.DateField()

    #Grupa
    OSOBISTE='OS'
    PRACA='PR'
    SZKOLA='SZ'
    grupy=[(OSOBISTE,'Osobiste'),(PRACA,'Praca'),(SZKOLA,'Szkola')]
    grupa = models.CharField(
        max_length=2,
        choices=grupy,
        default=OSOBISTE,
    )
    
    czas=models.CharField(
        max_length=5,
        default='01:00',
    )

    #zrobione
    TAK='tak'
    NIE='nie'
    zrobione=[(TAK,'Tak'),(NIE,'Nie')]
    zrobione = models.CharField(
        max_length=3,
        choices=zrobione,
    )

    