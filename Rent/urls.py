from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car/<int:car_id>/', views.car_detail, name='car'),
    # ex: /polls/5/results/
    path('client/<int:client_id>/', views.client_detail, name='client'),
    # ex: /polls/5/vote/
    path('rent/<int:rent_id>/', views.rent_detail, name='rent'),    
]


from rest_framework.routers import DefaultRouter
from Rent import views

router = DefaultRouter()
router.register(r'rest_car', views.CarViewSet)
router.register(r'rest_client', views.ClientViewSet)

#REST:

'''
urlpatterns = urlpatterns + [
    url(r'^rest_car/$', views.RestCarList.as_view()),
    url(r'^rest_car/(?P<pk>[0-9]+)/$', views.RestCarDetail.as_view()),
]
'''

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
    url(r'^', include(router.urls))
]


