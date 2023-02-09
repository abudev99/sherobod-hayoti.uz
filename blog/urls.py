from django.urls import path
from .views import newDetail, news,newspaperDetail

urlpatterns = [
    path('', news, name='home'),
    path('newspaper/<int:pk>', newspaperDetail, name='post_detail'),
    path('news/<int:pk>', newDetail, name='news_detail'),
]