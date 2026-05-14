from fastapi import FastAPI
import logging
import os
import requests

app = FastAPI()

# Create logs folder if not exists
os.makedirs("../logs", exist_ok=True)

log_file = os.path.abspath("../logs/api_logs.txt")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

@app.post("/create-order")
def create_order(order_id: int, item: str):

    logging.info(f"ORDER API STARTED | order_id={order_id} | item={item}")

    # Call Payment API
    payment_response = requests.post(
        "http://127.0.0.1:8001/process-payment",
        params={
            "order_id": order_id,
            "amount": 5000
        }
    )

    logging.info(
        f"PAYMENT API RESPONSE | status={payment_response.status_code}"
    )

    return {
        "message": "Order created successfully",
        "payment_status": payment_response.json()
    }