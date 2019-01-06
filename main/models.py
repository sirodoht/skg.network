from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Candidacy(models.Model):
    leader = models.CharField(max_length=300)
    party = models.CharField(max_length=300)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.leader


class Analytic(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    path = models.CharField(max_length=400, null=True, blank=True)
    querystring = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.ip
