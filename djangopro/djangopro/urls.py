"""djangopro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from djangoapp import views

product_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
]

product_patterns_id = [
    path("", views.products_id),
    path("comments", views.comments),
    path("questions", views.questions),
    path('characteristics',views.characteristics),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^about/contacts', views.contacts, name = 'home'),
    re_path(r'^about', views.about, name = 'home'),
    path('', views.index, name = 'home'),
    path("user/<str:name>/<int:id>", views.user_id),
    path("user/<str:name>", views.user),
    path("products/", include(product_patterns)),
    path("products/<int:id>/", include(product_patterns_id)),
    path('username/<str:name>/<int:age>',views.username),
    path("set", views.set),
    path("get", views.get),
    path('sample', views.sample_id),
    path('testsample', views.testsample),
    path('time', views.time),
    path('lang', views.lang),
    path('random', views.random_num),
    path('winners', views.winner),
    path('python', views.python),
    path('form', views.form),
    path('postuser/', views.postuser),


]


