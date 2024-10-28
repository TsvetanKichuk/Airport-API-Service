from django.urls import path, include
from rest_framework import routers

from airport.views import (
    AirplaneViewSet,
    FlightViewSet,
    TicketViewSet,
    OrderViewSet,
    CrewViewSet,
    RouteViewSet,
    AirportViewSet,
    AirplaneTypeViewSet,
)

router = routers.DefaultRouter()
router.register("airplanes", AirplaneViewSet)
router.register("flights", FlightViewSet)
router.register("tickets", TicketViewSet)
router.register("orders", OrderViewSet)
router.register("crews", CrewViewSet)
router.register("routs", RouteViewSet)
router.register("airports", AirportViewSet)
router.register("airplane-types", AirplaneTypeViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "airport"
