from django.urls import path
from . import views

from .views import SnippetViewSet
from rest_framework import renderers

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),

    path('snippets1/', views.SnippetList.as_view()),
    path('snippets1/<int:pk>/', views.SnippetDetail.as_view()),
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'snippets2', views.SnippetViewSet)
urlpatterns += [
    path('', include(router.urls)),
]