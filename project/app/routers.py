from rest_framework import routers
from app.views import StudentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('Student', StudentViewSet, basename='user')
urlpatterns = router.urls