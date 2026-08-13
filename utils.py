import httpx
from faker import Faker

from config import BASE_URL
from crm_client import CrmClient
from http_client import HttpClient

fake = Faker()


class BookingClient:
    @staticmethod
    def get_bookings() -> httpx.Response:
        return HttpClient.get(f"{BASE_URL}/booking")

    @staticmethod
    def get_booking(booking_id: int) -> httpx.Response:
        return HttpClient.get(f"{BASE_URL}/booking/{booking_id}")

    @staticmethod
    def create_booking(payload: dict) -> httpx.Response:
        return HttpClient.post(
            f"{BASE_URL}/booking",
            payload,
        )


def create_booking_payload() -> dict:
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=50, max=500),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": "2025-07-01",
            "checkout": "2025-07-10",
        },
    }


def create_booking_and_register() -> tuple[httpx.Response, httpx.Response]:
    payload = create_booking_payload()

    booking_response = BookingClient.create_booking(payload)

    booking = booking_response.json()

    crm_response = CrmClient.register_booking(booking)

    return booking_response, crm_response
