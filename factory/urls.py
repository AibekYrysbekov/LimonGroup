from django.urls import path, include
from rest_framework import routers
from . import views
from .views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)

urlpatterns = [

    path(
        'list-dailywork/',
        views.DailyWorkListAPIView.as_view(),
        name='list-dailywork'),
    path(
        'create-dailywork/<int:pk>/',
        views.DailyWorkCreateUpdateAPIView.as_view(),
        name='create-update-dailywork'),
    path(
        'destroy-dailywork/<int:pk>/',
        views.DailyWorkRetrieveDestroyAPIView.as_view(),
        name='destroy-dailywork'),
    path(
        'listcreate-neworder/',
        views.NewOrderListAPIView.as_view(),
        name='list-neworder'),
    path(
        'update-neworder/<int:pk>',
        views.NewOrderRetrieveUpdateAPIView.as_view(),
        name='update-neworder'),
    path(
        'destroy-neworder/<int:pk>/',
        views.NewOrderRetrieveDestroyAPIView.as_view(),
        name='destroy-neworder'),

    # SewingModel
    path(
        'Sewmodel-list-create/',
        views.sewingModel_list_create,
        name='Sewmodel-list-create'),
    path(
        'Sewmodel-update/<int:pk>/',
        views.sewingModel_ret_update,
        name='Sewmodel-ret-update'),

    path(
        'Sewmodel-destroy/<int:pk>/',
        views.sewingModel_ret_destroy,
        name='Sewmodel-ret-destroy'),

    # Price
    path(
        'price-list-create/',
        views.price_list_create,
        name='price-list-create'),
    path(
        'price-update/<int:pk>/',
        views.price_ret_update,
        name='price-ret-update'),
    path(
        'price-destroy/<int:pk>/',
        views.price_ret_destroy,
        name='price-ret-destroy'),

    # Storage

    path(
        'storage-list-create/',
        views.StorageListAPIView.as_view(),
        name='storage-list-create'),
    path(
        'storage-update/<int:pk>/',
        views.StorageRetrieveUpdateAPIView.as_view(),
        name='storage-ret-update'),
    path(
        'storage-destroy/<int:pk>/',
        views.StorageRetrieveDestroyAPIView.as_view(),
        name='storage-ret-destroy'),

    # RawStuff

    path(
        'rawstuff-list-create/',
        views.RawStuffListCreateAPIView.as_view(),
        name='rawstuff-list-create'),
    path(
        'rawstuff-update/<int:pk>/',
        views.RawStuffRetrieveUpdateAPIView.as_view(),
        name='rawstuff-ret-update'),
    path(
        'rawstuff-destroy/<int:pk>/',
        views.RawStuffRetrieveDestroyAPIView.as_view(),
        name='rawstuff-ret-destroy'),

    # FabricCutting

    path(
        'fabriccutting-list-create/',
        views.FabricCuttingListCreateAPIView.as_view(),
        name='fabriccutting-list-create'),
    path(
        'fabriccutting-update/<int:pk>/',
        views.FabricCuttingRetrieveUpdateAPIView.as_view(),
        name='fabriccutting-ret-update'),
    path(
        'fabriccutting-destroy/<int:pk>/',
        views.FabricCuttingRetrieveDestroyAPIView.as_view(),
        name='fabriccutting-ret-destroy'),

    #Order

    path('order/', include(router.urls), name='order'),    
  

    path('order/', include(router.urls), name='order'),
    

    # Quantity
   

    # Production
    path('production-per-day/', views.ProductionWork.as_view(), name="production")

]
    # # Order
    # path('order-create/<int:pk>/', OrderCreateUpdateAPIView.as_view(), name='order'),
    # path('order-create/', OrderListCreateAPIView.as_view(), name='order'),





