import argparse
from bot.place_order import OrderService

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    service = OrderService()

    response = service.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.qty,
        price=args.price
    )

    print("\nOrder Summary")
    print("-------------")
    print(f"Order ID      : {response['orderId']}")
    print(f"Status        : {response['status']}")
    print(f"Executed Qty  : {response['executedQty']}")
    print(f"Avg Price     : {response.get('avgPrice', 'N/A')}")
    print("✅ Order placed successfully")

if __name__ == "__main__":
    main()
