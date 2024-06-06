# Car App API

Welcome to the Car App API repository! This project provides a robust RESTful API for managing car-related data, including features for authentication, user management, and car information handling.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete functionality for car data.
- **Convenient Search**: Search data by different filters.
- **Modular Design**: Organized and scalable code structure.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vartan14/car-app-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd car-app-api
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the development server:
   ```bash
   python app.py
   ```
2. Access the API at `http://localhost:5000`.

## API Endpoints

- **Car Management**
  - `GET /cars/`: Get a list of all cars
  - `POST /add-car/`: Add a new car
  - `PUT /edit-car/<int:car_id>`: Edit a car by ID
  - `DELETE /delete-car/<int:car_id>`: Delete a car by ID
- **Owner Management**
  - `GET /owner/<int:owner_id>/`: Get owner details by ID
  - `POST /add-owner/`: Add a new owner
  - `PUT /edit-owner/<int:owner_id>/`: Edit an owner by ID
  - `DELETE /delete-owner/<int:owner_id>/`: Delete an owner by ID
- **Statistics**
  - `GET /statistics/`: Get statistics

## Requirements

- Python 3.x
- Flask
- Flask-RESTful
- Flask-JWT

