from django.shortcuts import render, redirect
from core.models import Note
import core.personality as p


# The home page that take in user input and gets the MBTI
def splash(request):
    if request.method == "POST":
        body = request.POST["body"]
        if len(body) == 0:
            return redirect("/")
        personality = str(p.logistic_regression(body))
        Note.objects.create(body=body, personality=personality)
    notes = Note.objects.all().order_by('-created_at')
    return render(request, "splash.html", {"notes": notes})


# Takes you to the analyze page that gives you MBTI description of that post
def analyze(request):
    if request.method == "POST":
        note_id = request.POST["note_id"]
    notes = Note.objects.filter(id=note_id)
    return render(request, "analyze.html", {"notes": notes})
