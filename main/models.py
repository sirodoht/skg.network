from django.db import models


class Candidacy(models.Model):
    leader = models.CharField(max_length=300)
    party = models.CharField(max_length=300)
    website = models.URLField()
