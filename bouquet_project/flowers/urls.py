from django.urls import path
from . import views

urlpatterns = [
    path('', views.bouquet_list, name='bouquet_list'),
    path('bouquet/<uuid:share_id>/', views.bouquet_detail, name='bouquet_detail'),
    path('bouquet/<uuid:share_id>/comment/', views.add_comment, name='add_comment'),
    path('bouquet/<uuid:share_id>/vote/', views.toggle_vote, name='toggle_vote'),
]