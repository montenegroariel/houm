from django.urls import path, include, register_converter
from .views import TimeViewSet, LocationViewSet, VelocityViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', LocationViewSet, basename='locations')

class FloatConverter:
    regex = '[\d\.\d]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return '{}'.format(value)
        
register_converter(FloatConverter, 'float')

urlpatterns = [
    path('time/<int:user_id>', TimeViewSet.as_view(), name='houmer-time'),
    path('velocity/<int:user_id>/<float:velocity>/', VelocityViewSet.as_view(), name='houmer-velocity'),
    path('', include(router.urls)),
]