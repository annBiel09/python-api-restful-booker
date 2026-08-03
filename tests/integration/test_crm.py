from crm_client import CrmClient


def test_register_booking():

    response = CrmClient.register_booking({"bookingid": 1, "firstname": "Anna"})

    assert response.status_code == 200
    assert response.json()["status"] == "registered"
