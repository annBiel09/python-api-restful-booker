import logging

from utils import BookingClient, create_booking_and_register, create_booking_payload

logger = logging.getLogger(__name__)


def test_booking_lifecycle():

    payload = create_booking_payload()

    create_response = BookingClient.create_booking(payload)

    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    logger.info(f"Created booking_id: {booking_id}")

    get_response = BookingClient.get_booking(booking_id)

    assert get_response.status_code == 200

    booking = get_response.json()

    logger.info(f"Retrieved booking: {booking}")

    assert booking["firstname"] == payload["firstname"]
    assert booking["lastname"] == payload["lastname"]
    assert booking["totalprice"] == payload["totalprice"]
    assert booking["depositpaid"] == payload["depositpaid"]
    assert booking["bookingdates"] == payload["bookingdates"]


def test_booking_registration_in_crm():

    booking_response, crm_response = create_booking_and_register()

    assert booking_response.status_code == 200
    assert crm_response.status_code == 200

    assert crm_response.json()["status"] == "registered"
