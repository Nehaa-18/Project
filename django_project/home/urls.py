from django.contrib import admin
from django.urls import path
from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index,name='home'),
    path('index.html', views.index,name='home'),
    path('login.html', views.login,name='login'),
    path('registration', views.registration,name='registration'),
    path('about.html', views.about,name='about'),
    path('contact.html', views.contact,name='contact'),
    path('product', views.product,name='product'),
    path('cart', views.cart,name='cart'),
    path('index',views.index,name="index"),
    path('admindash',views.admindash,name="admindash"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('dashboardOrg',views.dashboardOrg,name="dashboardOrg"),
    path('account',views.account,name="account"),
    path('order',views.order,name="order"),
    path('addequip',views.addequip,name="addequip"),
    path('view_equip',views.view_equip,name="view_equip"),
    path('usertypecount', views.usertypecount, name='usertypecount'),
    path('wishlist',views.wishlist,name="wishlist"),
    # Add a product to the wishlist
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    # Remove a product from the wishlist
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    path('rent',views.rent,name="rent"),
    path('accountorg',views.accountorg,name="accountorg"),
    #path('logout/', views.logout_view, name='logout'),

    #categories
    path('movingequip',views.movingequip,name="movingequip"),

    #path('admin_index/', views.admin_index, name='admin_index'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),


    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    #path('product/<int:product_id>/', views.product, name='product'),





    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
    #path('accounts/login/', views.login, name='login'),
    #path('accounts/registration/', views.registration, name='registration'),
    path('logout',views.logout,name="logout"),


   



]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

