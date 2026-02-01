import time
from bot.client import BinanceFuturesClient

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        # Futures mandatory setup
        self.client.set_margin_type(symbol)
        self.client.set_leverage(symbol, leverage=1)

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "positionSide": "BOTH",
            "timestamp": int(time.time() * 1000),
            "recvWindow": 60000,
            "newOrderRespType": "RESULT"
        }

        if order_type == "LIMIT":
            if price is None:
                raise ValueError("LIMIT order requires price")
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = self.client.post("/fapi/v1/order", params)

        if response.status_code != 200:
            raise Exception(f"{response.status_code} | {response.text}")

        return response.json()
