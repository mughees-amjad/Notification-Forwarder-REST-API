# Notification Forwarder Service

This project is a simple REST API that receives notification messages and forwards specific types to a Telegram channel.

It filters notifications based on their type: 
- Warnings are forwarded to Telegram.
- Info messages are ignored.

The goal of this project is to demonstrate API design, message handling, and basic integration with external services like Telegram.

## Features

- RESTful POST endpoint for receiving notifications.
- Filtering based on the "Type" field of incoming messages.
- Integration with Telegram using a bot.
- In-memory processing (no database).
- Includes tests using pytest.

## How it Works

When a service sends a POST request with a JSON body, the application checks the notification type. If it's a "Warning", it sends the message to a configured Telegram chat using the bot API. If it's "Info", the message is ignored.

## Technologies Used

- Python 3
- Flask (web server)
- `requests` (for sending messages to Telegram)
- `pytest` (for testing)

## How to Set Up and Run

1. **Clone or extract the repository**
   Make sure all files (`app.py`, `config.py`, etc.) are in the same folder.

2. **Create and activate a virtual environment**

   On Windows:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   On Linux/Mac:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages**

   ```
   pip install flask requests
   ```

4. **Update `config.py`**

   Add your own Telegram bot token and chat ID.

5. **Run the Flask server**

   ```
   python app.py
   ```

   The API will run on `http://127.0.0.1:5000/notify`

6. **Test the API**

   You can send a POST request using `curl` or Postman:

   Example:
   ```bash
   curl -X POST http://127.0.0.1:5000/notify -H "Content-Type: application/json" -d "{\"Type\": \"Warning\", \"Name\": \"CPU Overload\", \"Description\": \"Load too high\"}"
   ```

7. **Run Tests**

   To run unit tests:
   ```
   pytest test_app.py
   ```

## Notes

- All messages are handled in-memory.
- Authentication or error logging is not included to keep things simple.
- The `messenger.py` module is responsible for sending messages through Telegram.

## Author

Muhammad Mughees
