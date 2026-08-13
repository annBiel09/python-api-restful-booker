import logging

from utils import BookingClient, create_booking_payload

logger = logging.getLogger(__name__)


def test_get_booking_ids():
    response = BookingClient.get_bookings()

    assert response.status_code == 200


def test_get_booking():
    response = BookingClient.get_bookings()

    logger.info(f"Booking list (first 10): {response.json()[:10]}")

    booking_id = response.json()[0]["bookingid"]

    logger.info("Selected booking_id: %s", booking_id)

    booking = BookingClient.get_booking(booking_id)

    logger.info(f"Booking details: {booking.json()}")

    assert booking.status_code == 200


def test_create_booking():

    payload = create_booking_payload()

    response = BookingClient.create_booking(payload)

    assert response.status_code == 200

    booking = response.json()["booking"]

    assert booking["firstname"] == payload["firstname"]
    assert booking["lastname"] == payload["lastname"]
    assert booking["totalprice"] == payload["totalprice"]

    assert "bookingid" in response.json()
