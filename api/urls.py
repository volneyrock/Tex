from django.urls import path, include
from api.views import ConsultaCEPView
from api.views import PessoaView
from rest_framework.routers import DefaultRouter


app_name = "api"


urlpatterns = [
    path("cep/<str:cep>/", ConsultaCEPView.as_view(), name="consulta_cep"),
    path("pessoa/", PessoaView.as_view(), name="pessoa"),
    path("pessoa/<str:pk>/", PessoaView.as_view(), name="pessoa"),
]
