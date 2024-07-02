from django.urls import path
from .views import*

urlpatterns = [
    path('register',register,name="register"),
    path('',home,name="home"),
    path('about',about,name="about"),
    path('signin',signin,name='signin'),
    path('signout',signout,name='signout'),
    path('course_list',course_list, name='course_list'),
    path('profile/<str:username>',Detail.as_view(),name='Detail'),
    path('profile/update/<int:pk>',UpdateData.as_view(),name='update'),
    path('profile/ChangePassword/<int:pk>',ChangePassword.as_view(),name='ChangePassword'),
    path('forgot-password', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password', ResetPasswordView.as_view(), name='reset_password'),
    path('first-login', FirstLoginView.as_view(), name='first_login'),
    path('create-password', CreatePasswordView.as_view(), name='create_password'),
    path('activate/<uidb64>/<token>',activate, name='activate'),
    path('registration-success',registration_success, name='registration_success'),
    path('activation-success',activation_success, name='activation_success'),
    path('activation-invalid',activation_invalid, name='activation_invalid'),
    path('save-selected-courses', save_selected_courses, name='save_selected_courses'),
    path('delete-selected-course', delete_selected_course, name='delete_selected_course'),
    path('contact',contact_view,name='contact'),
    path('resend_activation_link',resend_activation_link, name='resend_activation_link'),
]