from fastapi import FastAPI
import logging
import os

app = FastAPI()

os.makedirs("../logs", exist_ok=True)

log_file = os.path.abspath("../logs/api_logs.txt")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

@app.post("/process-payment")
def process_payment(order_id: int, amount: float):

    logging.info(
        f"PAYMENT API CALLED | order_id={order_id} | amount={amount}"
    )

    return {
        "message": "Payment successful",
        "order_id": order_id,
        "amount": amount
    }