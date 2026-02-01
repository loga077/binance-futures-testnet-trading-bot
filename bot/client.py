import os
import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://testnet.binancefuture.com"

class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("API key / secret missing")

    def sign(self, params: dict) -> dict:
        query = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode(),
            query.encode(),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def post(self, endpoint: str, params: dict):
        signed = self.sign(params)
        headers = {"X-MBX-APIKEY": self.api_key}
        return requests.post(
            BASE_URL + endpoint,
            headers=headers,
            params=signed,
            timeout=10
        )

    # Futures required setup
    def set_margin_type(self, symbol: str):
        params = {
            "symbol": symbol,
            "marginType": "ISOLATED",
            "timestamp": int(time.time() * 1000),
            "recvWindow": 60000
        }
        self.post("/fapi/v1/marginType", params)

    def set_leverage(self, symbol: str, leverage: int = 1):
        params = {
            "symbol": symbol,
            "leverage": leverage,
            "timestamp": int(time.time() * 1000),
            "recvWindow": 60000
        }
        self.post("/fapi/v1/leverage", params)
