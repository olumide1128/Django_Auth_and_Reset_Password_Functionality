from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_view

app_name = 'reset'

urlpatterns = [
	path('reset_password/', auth_view.PasswordResetView.as_view(template_name="reset/password_reset.html", success_url=reverse_lazy('reset:password_reset_done')), name='reset_password'),
	path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(template_name="reset/password_reset_done.html"), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="reset/password_reset_confirm.html", success_url=reverse_lazy('reset:password_reset_complete')), name='password_reset_confirm'),
	path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name="reset/password_reset_complete.html"), name='password_reset_complete'),
]