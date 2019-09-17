from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from . import views

urlpatterns = [
    path("",views.homepage,name="home"),
    path("signup/",views.signup_page, name="signup_url"),
    path("login/", views.login_page, name="login_url"),
    path("product/", views.product_page, name="product_url"),
    path("about_us/",views.about_us, name="about_us_url"),
    path("services/", views.services_page, name="services_url"),
    path("reservation/", views.reservation_page, name="reservation_url"),


    url(r'^$', views.product_list,
        name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<product_id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail')

]
