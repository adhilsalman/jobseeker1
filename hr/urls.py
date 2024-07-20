from django.urls import path
from hr import views
urlpatterns=[
    path('signin',views.loginview.as_view(),name="signin"),
    path('index',views.dashboard.as_view(),name="index"),
    path('logout',views.signout.as_view(),name="logout"),
    path('create/',views.Addcategory.as_view(),name="category"),
    path('remove/<int:pk>',views.categoryremove.as_view(),name="category-del"),
    path('add',views.Addjob.as_view(),name="addjob"),
    path('removejob/<int:pk>',views.jobremove.as_view(),name="job-rem"),
    #path('jobview/<int:pk>',views.jobdetail.as_view(),name="job-det"),
    path('joblist/',views.joblist.as_view(),name="list"),
    path('jobedit/<int:pk>',views.jobupdate.as_view(),name="edit"),
    path('viewjobs/',views.Viewjobs.as_view(),name="viewjob"),
    path('application/<int:pk>',views.Seeker.as_view(),name="hrview")
]