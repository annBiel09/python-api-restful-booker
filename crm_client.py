import httpx

from config import CRM_BASE_URL


class CrmClient:
    @staticmethod
    def register_booking(booking: dict):
        response = httpx.post(f"{CRM_BASE_URL}/crm/booking", json=booking)

        response.raise_for_status()

        return response
