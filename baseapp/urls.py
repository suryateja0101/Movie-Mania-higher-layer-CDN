from django.urls import path
from . import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView
# )


urlpatterns = [
    path('hello/', views.getRoutes, name="routes"),
    path('hello/', views.getRoutes, name="routes"),
    path('hello/memberlist/', views.getmemberlist.as_view(), name="routes"),
    path('hello/member/', views.getmembers, name="routes"),
    path('hello/memberlist/<str:pk>', views.getmember, name="routes"),
    # custom Urls
    path('users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('users/getProfile/', views.getUserProfile,
         name='token_obtain_pair'),
    path('users/getUsers/', views.getUsers,
         name='token_obtain_pair'),
    path('users/register/', views.userRegister, name='token_obtain_pair'),


    # New changes goes here

    #
    path('member/register/', views.memberRegister, name="members"),
    path('member/login/', views.memberLogin, name="members"),
    path('member/homepage/', views.memberHomepage, name="members"),
    path('member/getProfile/', views.getMemberProfile, name="members"),
    path('member/updateDetails/', views.memberUpdateDetails, name="members"),
    path('member/viewTasks/',
         views.memberViewTasks, name="members"),

    path('organization/register/', views.organizationRegister, name="organizations"),
    path('organization/login/', views.organizationLogin, name="organizations"),
    path('organization/homepage/', views.organizationHomepage, name="organizations"),
    path('organization/getProfile/',
         views.getOrganizationProfile, name="organizations"),
    path('organization/updateDetails/',
         views.organizationUpdateDetails, name="organizations"),

    path('organization/createPost/',
         views.organizationCreatePost, name="organizations"),
    path('organization/updatePost/',
         views.organizationUpdatePost, name="organizations"),
    path('organization/viewMembers/',
         views.organizationViewMembers, name="organizations"),
    path('organization/viewPosts/',
         views.organizationViewPosts, name="organizations"),

    path('organization/createVideoPost/',
         views.createVideoPosts, name="organizations"),

    path('organization/updateVideoPost/',
         views.updateVideoPosts, name="organizations"),


]
