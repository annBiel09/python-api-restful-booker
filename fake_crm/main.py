from fastapi import FastAPI

app = FastAPI()


@app.post("/crm/booking")
def register_booking():
    return {"crmId": "CRM-12345", "status": "registered"}
