from django.shortcuts import render, redirect
from .forms import ContactForm, SubscriptionForm
from django.contrib import messages

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, "We have received your response you will be contacted shortly!!")
            return redirect('contact')
    else:
        return render(request, 'contact/contact.html')


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, "You have successfully subscribed to our newsletter!")
            redirect('index')
    else:
        return render(request, 'index.html')
