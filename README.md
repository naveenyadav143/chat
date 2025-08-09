## Task 4: Build a REST API with Flask

**Objective:**
Create a REST API that manages user data.

**Tools:**
- Python
- Flask
- Postman or Curl

**Deliverables:**
- Flask app with GET/POST/PUT/DELETE routes

**Hints/Mini Guide:**
1. Use Flask to create endpoints
2. Store users in a dictionary or in-memory list

**Outcome:**
Learn API development fundamentals

## WebScarp Project

This project contains two main components:

- **scarp.py**: A script to scrape headlines from BBC News and save them to a file.
- **app.py**: A simple Flask REST API for managing users (CRUD operations).

### app.py - Flask User API

This API allows you to manage users in memory. Available endpoints:

- `GET /users` — List all users
- `GET /users/<user_id>` — Get a user by ID
- `POST /users` — Add a new user (JSON: `{ "name": "username" }`)
- `PUT /users/<user_id>` — Update a user's name (JSON: `{ "name": "newname" }`)
- `DELETE /users/<user_id>` — Delete a user by ID

Example usage with curl:

```bash
# Add a user
curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice"}' http://127.0.0.1:5000/users

# List users
curl http://127.0.0.1:5000/users

# Get user 1
curl http://127.0.0.1:5000/users/1

# Update user 1
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Bob"}' http://127.0.0.1:5000/users/1

# Delete user 1
curl -X DELETE http://127.0.0.1:5000/users/1
```

---
## WebScarp Project

This project contains two main components:

- **scarp.py**: A script to scrape headlines from BBC News and save them to a file.
- **app.py**: A simple Flask REST API for managing users (CRUD operations).

### Requirements

- Python 3.x
- Flask
- requests
- beautifulsoup4

Install dependencies:

```bash
pip install flask requests beautifulsoup4
```

### Usage

#### Run the Flask API

```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000/`.

#### Run the Web Scraper

```bash
python scarp.py
```
This will save BBC News headlines to `headlines.txt`.

---
Feel free to modify and extend this project!
