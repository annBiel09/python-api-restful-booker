import httpx
from faker import Faker

from config import BASE_URL
from crm_client import CrmClient

fake = Faker()


class Booking:
    @staticmethod
    def _get(url: str) -> httpx.Response:
        response = httpx.get(url)
        response.raise_for_status()
        return response

    @staticmethod
    def _post(url: str, payload: dict) -> httpx.Response:
        response = httpx.post(url, json=payload)
        response.raise_for_status()
        return response

    @staticmethod
    def get_bookings():
        return Booking._get(f"{BASE_URL}/booking")

    @staticmethod
    def get_booking(booking_id: int) -> httpx.Response:
        return Booking._get(f"{BASE_URL}/booking/{booking_id}")

    @staticmethod
    def create_booking(payload: dict) -> httpx.Response:
        return Booking._post(
            f"{BASE_URL}/booking",
            payload,
        )


def create_booking_payload() -> dict:
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=50, max=500),
        "depositpaid": fake.boolean(),
        "bookingdates": {"checkin": "2025-07-01", "checkout": "2025-07-10"},
    }


def create_booking_and_register() -> tuple[httpx.Response, httpx.Response]:

    payload = create_booking_payload()

    booking_response = Booking.create_booking(payload)

    booking = booking_response.json()

    crm_response = CrmClient.register_booking(booking)

    return booking_response, crm_response
