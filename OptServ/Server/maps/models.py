from django.db import models

class Bunker(models.Model):
    id = models.IntegerField(primary_key = True)
    coordinat1 = models.IntegerField()
    coordinat1D = models.IntegerField(default=0)
    coordinat2 = models.IntegerField()
    coordinat2D = models.IntegerField(default=0)
    Full = models.IntegerField()
    remove = models.BooleanField()

    def filter():
        if Bunker.Full > 75:
            return(True)
