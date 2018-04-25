from django.shortcuts import render, redirect

# Create your views here.
def external(request):
    return render(request, 'websites/external.html', {'nbar':'external'})

def english(request):
    return render(request, "websites/english.html", {'nbar':'english'})

def contact(request):
    return render(request, 'websites/contact.html', {'nbar':'contact'})

def music(request):
    return render(request, 'websites/music.html', {'nbar':'music'})

def about(request):
    return render(request, 'websites/about.html', {'nbar':'about'})

def courses(request):
    return render(request, 'websites/courses.html', {'nbar':'courses'})

def faq(request):
    return render(request, 'websites/faq.html', {'nbar':'faq'})
