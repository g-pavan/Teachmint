# Expense Splitter App

This Flask application is designed to split expenses among users in various ways: equally, with exact amounts, or based on percentages. The application provides endpoints to handle different splitting scenarios and maintain balances for each user.

## Architecture Diagram

```
            +-----------+       +-----------------------+
            |           |       |                       |
            |   Client  |<----->|       Flask App       |
            |           |       |                       |
            +-----------+       +-----------------------+
                                    |           |        
                                    |           |        
                                    |           |        
                                +---+---+   +---+---+
                                |       |   |       |
                                |  User |   |  User |
                                |       |   |       |
                                +-------+   +-------+
```

## API Contracts

### Split Equal Endpoint

- **URL:** `/split_equal`
- **Method:** POST
- **Request Body:**
  ```json
  {
      "payer_id": "string",
      "payer_amount": float,
      "participants_details": [
          {
              "participant_id": "string",
              "participant_name": "string",
              "participant_email": "string",
              "participant_phone": "string"
          },
          ...
      ]
  }
  ```
- **Response Body (Success):**
  ```json
  {
      "message": "Expense split equally among participants"
  }
  ```
- **Response Body (Error):**
  ```json
  {
      "Error": "string"
  }
  ```

### Split Exact Endpoint

- **URL:** `/split_exact`
- **Method:** POST
- **Request Body:**
  ```json
  {
      "payer_id": "string",
      "payer_amount": float,
      "participants_details": [
          {
              "participant_id": "string",
              "participant_amount": float
          },
          ...
      ]
  }
  ```
- **Response Body (Success):**
  ```json
  {
      "message": "Expense split with exact amounts among participants"
  }
  ```
- **Response Body (Error):**
  ```json
  {
      "Error": "string"
  }
  ```

### Split Percentages Endpoint

- **URL:** `/split_percentages`
- **Method:** POST
- **Request Body:**
  ```json
  {
      "payer_id": "string",
      "payer_amount": float,
      "participants_details": [
          {
              "participant_id": "string",
              "participant_percentage": float
          },
          ...
      ]
  }
  ```
- **Response Body (Success):**
  ```json
  {
      "message": "Expense split based on percentages among participants"
  }
  ```
- **Response Body (Error):**
  ```json
  {
      "Error": "string"
  }
  ```

### Show Balance Endpoint

- **URL:** `/show_balance/<user_id>`
- **Method:** GET
- **Response Body (Success):**
  ```json
  {
      "message": "User ID: User"
  }
  ```
- **Response Body (Error):**
  ```json
  {
      "Error": "string"
  }
  ```



## Classes and Interfaces

The application includes a `User` class with methods to handle spending and owing amounts. Additional classes can be implemented to manage expenses and balances effectively.