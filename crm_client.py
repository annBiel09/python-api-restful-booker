from config import CRM_BASE_URL
from http_client import HttpClient


class CrmClient:
    @staticmethod
    def register_booking(booking: dict):
        return HttpClient.post(
            f"{CRM_BASE_URL}/crm/booking",
            booking,
        )
