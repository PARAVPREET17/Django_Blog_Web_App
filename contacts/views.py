from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def contact(request):
    form=ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"We have received your response you will be contacted shortly!!")
            return redirect('contact')
    else:
        return render(request, 'contact/contact.html')    