"""
By Jeffrey Kotz - 2/20/2026
This file defines Views for the Movie Theater Booking App
"""

# from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from bookings.models import Movie, Seat, Booking
from bookings.serializers import (MovieSerializer,
                                  SeatSerializer,
                                  BookingSerializer)

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

        Returns:
            Response: indicating whether seat was booked or not
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

    @action(detail=False, methods=["GET"])
    def booking_history(self, request):
        """Obtain all existing bookings

        Args:
            request (HttpRequest): Request for booking history

        Returns:
            Response: Response of all past bookings
        """
        return self.list(request)

    @action(detail=False, methods=['GET', 'POST'])
    def create_booking(self, request):
        """Create a booking, overridden from ViewSet creat method

        Args:
            request (HttpRequest): request given with information on booking
                                   to create

        Returns:
            Response: _description_
        """

        serializer = BookingSerializer(data=request.data)
        response = Response({'status': status.HTTP_400_BAD_REQUEST})

        # Check if valid request was made
        if serializer.is_valid():

            movie = serializer.validated_data['movie']
            seat = serializer.validated_data['seat']
            booking_date = serializer.validated_data['booking_date']

            # If the release date preceeds the current time, then the movie
            # can be booked
            if movie.release_date < booking_date:

                # This is entirely unecessary since seats have a one to one
                # relationship with bookings, but I left it here just in case
                # there might be some other reason a seat is unavailable
                # Maybe it's damaged/broken?
                if not seat.booking_status:
                    seat.booking_status = True
                    seat.save()
                    response = self.create(request)  # create the booking\
                else:
                    response = Response({'status': 'Seat Unavailable'})
            else:
                response = Response({'status': f'Booking on {booking_date} is '
                                     f'before movie is released '
                                     f'on {movie.release_date}'})
        return response
