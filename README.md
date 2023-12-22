# API Name

This API provides endpoints to manage situations and users.

## Description

This API allows users to perform CRUD operations (Create, Read, Update, Delete) on situations and users.

## Endpoints

### Users

- `GET /users`
  - Description: Retrieve all users.
- `GET /users/<user_id>`
  - Description: Retrieve a specific user by ID.
- `POST /users`
  - Description: Create a new user.
- `PUT /users/<user_id>`
  - Description: Update a specific user by ID.
- `DELETE /users/<user_id>`
  - Description: Delete a specific user by ID.

### Situations

- `GET /situations`
  - Description: Retrieve all situations.
- `GET /situations/<situation_id>`
  - Description: Retrieve a specific situation by ID.
- `POST /situations`
  - Description: Create a new situation.
- `PUT /situations/<situation_id>`
  - Description: Update a specific situation by ID.
- `DELETE /situations/<situation_id>`
  - Description: Delete a specific situation by ID.

## Usage

### Prerequisites

- Python (version X.X)
- Flask (version X.X)
- Python-dotenv (version X.X)
- (Any other dependencies)

### Installation

1. Clone this repository.

follow this steps :

```
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 run.py

```
