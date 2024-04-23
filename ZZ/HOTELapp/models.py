from django.db import models

class Buffet(models.Model):
    horario = models.CharField(max_length=100)
    menu = models.TextField()

    def __str__(self):
        return self.horario