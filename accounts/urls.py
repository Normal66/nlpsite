from django.urls import path, include
from .views import NLPLoginView, NLPLogoutView, ChangeUserlnfoView, NLPPasswordChangeView, profile, \
    RegisterUserView, RegisterDoneView, user_activate, DeleteUserView

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', NLPLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', NLPLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangeUserlnfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', NLPPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/асtivate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
]
