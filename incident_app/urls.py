from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('incident', IncidentView, basename='incident')
urlpatterns = router.urls