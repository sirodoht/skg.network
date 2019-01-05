from django.shortcuts import redirect, render

from main import models


def index(request):
    return redirect("main:elections")


def elections(request):
    candidacies = models.Candidacy.objects.all().order_by("id")
    return render(request, "main/layout.html", {"candidacies": candidacies})
