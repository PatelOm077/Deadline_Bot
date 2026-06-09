# Deadline Bot

A FastAPI-based task management API that sends WhatsApp reminders via Twilio when your deadlines are approaching or missed.

## What It Does

- **CRUD API** for managing tasks with name, deadline, and priority
- **Background scheduler** checks deadlines every 5 minutes
- **WhatsApp reminder** sent when a deadline is within 1 hour
- **Overdue alert** sent via WhatsApp if the deadline has passed

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — REST API
- [SQLAlchemy](https://www.sqlalchemy.org/) + SQLite — database
- [Twilio](https://www.twilio.com/) — WhatsApp messages
- [APScheduler](https://apscheduler.readthedocs.io/) — background job scheduling

## Setup

### 1. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy twilio apscheduler python-dotenv
```

### 2. Configure environment variables

Create a `.env` file in the project root:

```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_SID=your_auth_token
TWILIO_NUMBER=whatsapp:+14155238886
MY_NUMBER=whatsapp:+your_number
```

### 3. Run the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.  
Interactive docs at `http://127.0.0.1:8000/docs`.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/tasks` | Create a new task |
| `GET` | `/tasks` | Get all tasks |
| `GET` | `/tasks/{id}` | Get a single task |
| `PUT` | `/tasks/{id}` | Update a task |
| `DELETE` | `/tasks/{id}` | Delete a task |

### Task fields

```json
{
  "name": "Submit assignment",
  "deadline": "2026-06-10T18:00:00",
  "priority": "high",
  "is_done": false
}
```

`priority` can be any string (e.g. `low`, `medium`, `high`).

## How Reminders Work

The scheduler runs `check_deadline()` every 5 minutes:

- If a task's deadline is **within the next 60 minutes** and it hasn't been reminded yet → sends a WhatsApp reminder and marks `reminded = true`
- If a task's deadline has **already passed** and it hasn't been flagged yet → sends an overdue alert and marks `overdue = true`
