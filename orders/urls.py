from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('<int:option>/regular', views.regular_view, name='regular_view'),
    path('<int:option>/sicilian', views.sicilian_view, name='sicilian_view'),
    path('<int:option>/sub', views.sub_view, name='sub_view'),
    path('pastas', views.pasta_view, name='pasta_view'),
    path('salads', views.salad_view, name='salad_view'),
    path('<int:option>/dinner', views.dinner_view, name='dinner_view'),
    path('<int:pizza_id>/add-regular', views.add_regular, name='add_regular'),
    path('<int:pizza_id>/add-sicilian', views.add_sicilian, name='add_sicilian'),
    path('<int:sub_id>/add-sub', views.add_sub, name='add_sub'),
    path('<int:pasta_id>/add-pasta', views.add_pasta, name='add_pasta'),
    path('<int:salad_id>/add-salad', views.add_salad, name='add_salad'),
    path('<int:dinner_id>/add-dinner', views.add_dinner, name='add_dinner'),
    path('confirm', views.confirm_view, name='confirm_view'),
    path('orders', views.orders_view, name='orders_view'),
    path('<int:order_id>/view-order', views.view_order, name='view_order'),
    path('<int:id>/complete', views.complete, name='complete'),
    path('<int:id>/remove', views.remove, name='remove')
]
