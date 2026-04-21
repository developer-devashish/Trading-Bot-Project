# Trading Bot (Binance Demo API)

A CLI-based Python trading bot that places **MARKET** and **LIMIT** orders using the Binance **Demo Trading API**. It features a clean design, input checks, organized logging, and strong error handling.

---

## Objective

* Place orders through the CLI
* Support BUY / SELL, MARKET / LIMIT
* Provide clear outputs and logs
* Follow a modular code structure suited for production

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py        # API client (HMAC signing and request handling)
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation
│   └── logging_config.py
│
├── cli.py               # CLI entry point
├── .env                 # API credentials (not committed)
├── requirements.txt
└── logs/
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/developer-devashish/Trading-Bot-Project
cd trading_bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` file

```env
API_KEY=your_api_key
API_SECRET=your_secret_key
```

> Do NOT commit `.env` to GitHub.

---

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## Sample Output

```
Order Summary:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': '0.001', 'price': None}

Order Successful
Order ID: 12345678
Status: FILLED
Executed Qty: 0.001
Avg Price: 60000
```

---

## Features

* MARKET and LIMIT order support
* BUY and SELL support
* CLI argument parsing using argparse
* Input validation for type, side, quantity, and price
* Structured logging to a file
* Error handling for API issues and invalid input
* Modular code design

---

## Logging

* Logs are stored in:

```
logs/app.log
```

* Includes:

  * API requests
  * API responses
  * Errors

---

## Important Note (API Environment)

Due to recent changes in Binance:

* The original **Futures Testnet UI now directs to Demo Trading**
* Demo Trading uses **Spot-style API endpoints**
* This project uses:

```
https://demo-api.binance.com
```

instead of:

```
https://testnet.binancefuture.com
```

---

## Technical Highlights

* Manual **HMAC SHA256 signing**
* Timestamp synchronization using server time
* Clear separation of concerns:

  * API layer
  * Business logic
  * CLI layer

---

## Error Handling

Handles:

* Invalid input values
* Errors in API responses
* Timestamp mismatch issues
* Network failures

---

## Requirements

```txt
requests
python-dotenv
```

---

## Future Improvements (Optional)

* Stop-Limit orders
* Interactive CLI (menu-based)
* Web UI dashboard
* Strategy-based trading

---

## Author

Devashish Ghosh

---

## Evaluation Checklist

| Criteria        | Status |
| --------------- | ------ |
| Order placement | ✅      |
| Code structure  | ✅      |
| Validation      | ✅      |
| Logging         | ✅      |
| CLI usability   | ✅      |

---