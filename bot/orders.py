def place_order(client, symbol, side, order_type, quantity, price=None):
    if order_type == "MARKET":
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            recvWindow=60000
        )

    return client.futures_create_order(
        symbol=symbol,
        side=side,
        type=order_type,
        quantity=quantity,
        price=price,
        timeInForce="GTC",
        recvWindow=60000
    )
