from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # Regular Django APIs
    path('reg-django/users/', views.user_list),
    path('reg-django/users/<int:user_id>/', views.user_detail),
    path('reg-django/get-user/', views.get_user, name='get_user_by_contact'), # function based view
    path('reg-django/get-user-view/', views.GetUserView.as_view()), # class based view
    
    # Cache view
    path('reg-django/cache_view/<int:user_id>/', views.cache_view),
    
    # REST APIs
    path('api/users/', views.UserView.as_view(), name='create_user'), #POST
    path('api/users/<int:user_id>/', views.UserView.as_view(), name='user_detail'), # GET/PUT/PATCH/DELETE
    
]