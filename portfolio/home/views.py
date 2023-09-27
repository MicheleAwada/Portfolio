from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def home(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        print("test")
        if form.is_valid():
            print(form.cleaned_data)
            print("yes")
            form.save()
            messages.success(request, "Horray! Your message has been sent!")
            return redirect("/")
    else:
        form = ContactForm()
    context = {"form":form}
    return render(request, "home/index.html", context)