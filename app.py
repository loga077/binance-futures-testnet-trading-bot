import streamlit as st
from bot.place_order import OrderService

st.set_page_config(page_title="Binance Futures Testnet Bot", layout="centered")

st.title("📈 Binance Futures Testnet Trading Bot")

service = OrderService()

# ---- UI Inputs ----
symbol = st.text_input("Symbol", value="BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.number_input("Quantity", min_value=0.001, step=0.001, value=0.003)

price = None
if order_type == "LIMIT":
    price = st.number_input("Limit Price", min_value=1.0, step=10.0)

# ---- Submit ----
if st.button("🚀 Place Order"):
    try:
        response = service.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        st.success("Order placed successfully ✅")
        st.json({
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A")
        })

    except Exception as e:
        st.error(str(e))
