````md
# 📈 Binance Trading Bot (Python)

A simple Python-based trading bot that allows users to place **MARKET** and **LIMIT** orders on the Binance Demo API using secure API authentication.

Objective
Place orders through the CLI
Support BUY / SELL, MARKET / LIMIT
Provide clear outputs and logs
Follow a modular code structure suited for production

---

# 🚀 Features

- ✅ Place BUY and SELL orders
- ✅ Supports MARKET and LIMIT orders
- ✅ Binance API request signing using HMAC SHA256
- ✅ Environment variable support using `.env`
- ✅ Input validation for safe order placement
- ✅ Logging system for tracking bot activity
- ✅ Modular and maintainable project structure

---

# 📂 Project Structure

```bash
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── app.log
│
├── .env
├── .gitignore
├── cli.py
├── README.md
└── requirements.txt
````

---

# ⚙️ Technologies Used

* Python
* Binance Demo API
* Requests
* Dotenv
* Logging Module
* HMAC SHA256 Authentication

---

# 🔑 Setup Instructions

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/trading_bot.git
cd trading_bot
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory.

```env
API_KEY=your_binance_api_key
API_SECRET=your_binance_api_secret
```

---

# ▶️ Run the Bot

```bash
 python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --mode sell


```
# 🧠 How It Works

## 🔹 API Client

The `client.py` file handles:

* Binance API connection
* Request signing
* Timestamp generation
* Sending authenticated requests



---

## 🔹 Order Placement

The `orders.py` module creates and sends MARKET or LIMIT orders.



---

## 🔹 Validation System

The `validators.py` module validates:

* BUY / SELL side
* MARKET / LIMIT order type
* Quantity
* Price validation for LIMIT orders



---

## 🔹 Logging

The project automatically creates logs inside:

```bash
logs/app.log
```

Logging setup:



---

# 📌 Example Order Flow

```text
1. User enters trading details
2. Input gets validated
3. Request is signed securely
4. Order is sent to Binance Demo API
5. Response is displayed
6. Activity gets logged
```

---

# 👨‍💻 Author

**Devashish Ghosh**

* Python Developer
* Cloud & Automation Enthusiast

---

# 📜 License

This project is licensed under the MIT License.

```
```
