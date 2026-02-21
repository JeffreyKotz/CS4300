"""
By Jeffrey Kotz - 2/20/2026
This file defines Views for the Movie Theater Booking App
"""

# from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from bookings.models import Movie, Seat, Booking
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    """Movie View Set implementing CRUD operations
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    # As MovieViewSet is a derived class from ModelViewSet it implement: list,
    # create, retrieve, update, partial_update, and destroy by default
    # No additional work is needed CRUD operations are built in


class SeatViewSet(viewsets.ModelViewSet):
    """Seat View Set for seat availability and booking status
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.AllowAny]

    # it is a GET operation, applied to all seats so detail=False
    @action(detail=False, methods=["GET"])
    def available_seats(self, request) -> Response:
        """Find all seats available

        Args:
            request (HttpRequest): request given for available seats

        Returns:
            Response: response including all available seats Serialized as JSON
        """
        available_seats = Seat.objects.filter(booking_status=False)

        # if the query can be paginated, reutnr paginated response
        page = self.paginate_queryset(available_seats)
        if page is not None:
            # page exists. serialize page
            seralizer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(seralizer.data)
        else:
            # Else return non-paginated response
            serializer = self.get_serializer(available_seats, many=True)
            response = Response(serializer.data)
        return response

    # Book a seat, detail=True as we refer to a single seat
    @action(detail=True, methods=['GET'])
    def book_seat(self, request, pk=None):
        """book a seat of a given key

        Args:
            request (HttpRequest): the request given to book the seat
            pk (int, optional): primary key of the seat. Defaults to None.
        """
        seat = self.get_object()
        if not seat.booking_status:
            seat.booking_status = True
            response = Response({'status': 'seat booked'})
            seat.save()
        else:
            response = Response({'status': 'seat unavailable'})

        return response


class BookingViewSet(viewsets.ModelViewSet):
    """Booking View Set for users to book seats and view booking history
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    def booking_history(self):
        pass

    def create_booking(self):
        pass
