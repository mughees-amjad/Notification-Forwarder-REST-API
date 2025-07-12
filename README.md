# Notification Forwarder

This is a simple RESTful web service built using Flask that receives notification messages and forwards them to a Telegram channel if the notification type is "Warning". This project is intended to demonstrate basic system design, API handling, message filtering, and third-party integration.

## Features

- Accepts POST requests with notification payloads
- Filters and forwards "Warning" type messages to a Telegram channel
- Ignores "Info" type messages
- Built with a simple and modular Python structure
- Includes test coverage using `pytest`

## Files Included

- `app.py`: Main Flask application handling incoming API requests
- `messenger.py`: Logic to send messages to the Telegram bot
- `test_app.py`: Unit tests to verify the service behavior
- `config_example.py`: Template configuration file (credentials are excluded for security)
- `README.md`: This documentation

## Configuration

To run the project, you need your own Telegram bot token and chat ID.

1. Open the file `config_example.py`
2. Replace the placeholders with your actual credentials:

3. Rename the file from `config_example.py` to `config.py`

Note: Do not share your real `config.py` file publicly, as it contains sensitive credentials.

## How to Run the App

### 1. Set up your environment

Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Start the Flask server

```bash
python app.py
```

This will start the server at `http://127.0.0.1:5000`

### 3. Send a test POST request

You can use `curl` or Postman. Here's a curl example:

```bash
curl -X POST http://127.0.0.1:5000/notify   -H "Content-Type: application/json"   -d '{"Type": "Warning", "Name": "CPU Overload", "Description": "Load too high"}'
```

You should see a response confirming the message was forwarded.

## Running the Tests

To run the tests:

```bash
pytest test_app.py
```

Make sure you are in the virtual environment when running this command.

