from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
    
    
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world ! ")

from django.urls import path
from . import views

urlpatterns = [path('hello/', views.hello, name='hello'),]

from django.urls import include, path

urlpatterns = [path('myapp/', include('myapp.urls')),]