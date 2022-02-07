from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('generate-plan', views.generate_plan, name='generate-plan'),
    path('review', views.review_plan, name='review_plan'),
    path('plans-list', views.plans_list, name='plans-list'),
    path('compare-plan', views.compare_plan, name='compare-plan'),
    path('release-plan', views.compare_plan, name='release-plan')
]
