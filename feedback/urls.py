from django.urls import path, include
from . import views
from .views import FeedbackAdd, FeedbackHome, FeedbackCategory

urlpatterns = [
    path('', FeedbackHome.as_view(), name='fb-home'),
    path('about/', views.about, name='fb-about'),
    path('add/', FeedbackAdd.as_view(), name='fb-add'),
    path('category/<int:category_pk>/', FeedbackCategory.as_view(), name='fb-category'),
    path('feedback/<slug:fb_slug>', views.FeedbackDetail.as_view(), name='fb-detail'),
]
