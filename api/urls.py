from django.urls import path
from api.views import ConsultaCEPView


app_name = "api"


urlpatterns = [
    path("cep/<str:cep>/", ConsultaCEPView.as_view(), name="consulta_cep"),
]