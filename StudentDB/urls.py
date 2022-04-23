"""StudentDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from StudentApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('Add_Students',views.Add_Students),
    path('',views.index),
    path('View_Students',views.View_Students),
    path('Student_Update/<int:id>',views.Student_Update),
    path('Delete_Student/<int:id>',views.Delete_Student),
    path('add_user',views.add_user),
    path('login',views.login_fun),
    path('Registration',views.Registration_Fun),
    path('Admin_Page',views.Admin_Page),
    path('View_Registration',views.View_Registration),
    path('logout',views.logout_fun),
    path('Std_Reg_pro/<int:id>',views.Std_Reg_pro),
    path('User_pro',views.User_pro),
    path('Full_Details/<int:id>',views.Full_Details),
    path('About_Us',views.About_Us),
    path('Contact_Us',views.Contact),
    path('Show_Msg',views.Show_Msg),
    path('Rg_Msg',views.Rg_Msg),
    path('Admission_delete/<int:id>',views.Admission_delete),
    path('Pub_msg_delete/<int:id>',views.Pub_msg_delete),
    # path('Result_import',views.Result_import),
    path('Add_notis',views.Add_notis),
    # path('Event',views.Event),
    path('del_notis/<int:id>',views.del_notis),
    path('del_event/<int:id>',views.del_event),
    path('Add_Event',views.Add_Event),
    path('Event',views.Show_Event),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete')


]
