from allauth.socialaccount.providers.github.views import oauth2_login
from django.contrib import admin
from django.urls import include, path

from profiles.views import GitHubLogin, UserDetails

urlpatterns = [
    path("", oauth2_login, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/registration/", include("dj_rest_auth.registration.urls")),
    path("accounts/github/", GitHubLogin.as_view(), name="github_login"),
    path("accounts/profile/", UserDetails.as_view()),
    path("accounts/", include("allauth.urls")),
]
