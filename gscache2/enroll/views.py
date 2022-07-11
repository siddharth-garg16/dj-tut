from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
#we can cache multiple views...simple example here...don't need to vhange the middleware settings like persite cache but cache variable still needed to tell what type of cache is needed (db, file, local memory)
@cache_page(150)
def home(request):
    return render(request, 'enroll/courses.html')
