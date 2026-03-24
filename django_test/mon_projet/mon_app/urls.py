from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserViewSet, EventViewSet, ParticipantViewSet, RegistrationViewSet

router = DefaultRouter()
router.register('users',         UserViewSet,         basename='user')
router.register('events',        EventViewSet,        basename='event')
router.register('participants',  ParticipantViewSet,  basename='participant')
router.register('registrations', RegistrationViewSet, basename='registration')

urlpatterns = [
    # Auth JWT
    path('auth/login/',   TokenObtainPairView.as_view(),  name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(),     name='token_refresh'),

    # API CRUD
    path('', include(router.urls)),
]

# ─────────────────────────────────────────
# Dans ton fichier principal mon_projet/urls.py, ajoute :
#
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('mon_app.urls')),
# ]
# ─────────────────────────────────────────
