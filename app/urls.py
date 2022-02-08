from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('user/add', views.add_user, name="add_user"),
    path('user/list', views.user_list, name="user_list"),
    path('', views.index, name='index'),

    path('generate-plan/', views.generate_plan, name='generate-plan'),
    path('review/', views.review_plan, name='review_plan'),
    path('plans-list/', views.plans_list, name='plans-list'),
    path('compare-plan/', views.compare_plan, name='compare-plan'),
    path('release-plan/', views.compare_plan, name='release-plan')
]
