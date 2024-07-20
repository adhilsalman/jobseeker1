from django.urls import path
from user import views

urlpatterns = [
    path("reg/",views.Register.as_view(),name="reg"),
    path("user_login/",views.Student_home.as_view(),name="userindex"),
    path("profile/",views.user_profile.as_view(),name="profile"),
    path("p_view/<int:pk>",views.Profileview.as_view(),name="userview"),
    path("edit/<int:pk>",views.update_profile.as_view(),name="edit"),
    path('logout',views.signout.as_view(),name="userlogout"),
    path("detail/<int:pk>",views.jobdetailsview.as_view(),name="jobdetail"),
    path("applyjob/<int:pk>",views.Applyviewjob.as_view(),name="apply"),
    path("appledjob/",views.Appliedjob.as_view(),name="applied"),
    path("deljob/<int:pk>",views.deljob.as_view(),name="deljob")
]