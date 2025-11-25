# Hotel Management System (HMS)

## Overview
The Hotel Management System (HMS) is a console-based Python application designed to streamline the daily operations of a hotel. [cite_start]It automates manual processes such as guest check-in, room allocation, service ordering, and billing, reducing errors and improving operational efficiency[cite: 90].

## Features
* **Guest Check-In:** Captures guest details and automatically assigns unique room numbers.
* **Room Service:** Allows guests to order food/drinks, updating their bill dynamically.
* **Live Status:** Displays a list of currently occupied rooms and guest details.
* [cite_start]**Check-Out & Billing:** Calculates the total cost (Rent + Food) and generates a printed receipt upon checkout[cite: 92].

## Technologies Used
* **Language:** Python 3.9.0
* **Libraries:** `datetime`, `random` (Standard Library)
* [cite_start]**Data Structures:** Dictionaries (Hash Maps) for O(1) data retrieval[cite: 93].

## Steps to Install & Run
1.  **Prerequisites:** Ensure Python 3.9.0 is installed on your machine.
2.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/yourusername/hotel-management-system.git](https://github.com/yourusername/hotel-management-system.git)
    ```
3.  **Navigate to Directory:**
    ```bash
    cd hotel-management-system
    ```
4.  **Run the Application:**
    ```bash
    python main.py
    ```
    [cite_start]*(Note: Replace `main.py` with your actual filename)*[cite: 94].

## Testing Instructions
1.  **Test Check-In:** Select Option 1. Enter valid text for names and numbers for phones. Verify a Room ID is returned.
2.  **Test Service:** Select Option 2. Enter the Room ID generated in step 1. Order an item and ensure no crash occurs.

3.  **Test Validation:** Try entering a non-existent Room ID in "Check-Out". [cite_start]The system should display an error message rather than crashing[cite: 95].
