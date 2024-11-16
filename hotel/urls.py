from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import GetHotelsApiView

router = SimpleRouter()
router.register("hotels", GetHotelsApiView)

urlpatterns = [
] + router.urls
