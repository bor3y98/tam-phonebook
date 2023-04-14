# Phonebook Django Application

This is a simple phonebook Django application that allows you to create contacts with their related phone numbers.

## Prerequisites

- Docker
- Docker Compose

## Installation

1. Clone the repository to your local machine:
    ```bash
     git clone git@github.com:bor3y98/tam-phonebook.git
    ```
2. Create a `.env` file in the root directory of the project with the following contents:
    ```bash
   POSTGRES_USER=<your-postgres-username>
    POSTGRES_PASSWORD=<your-postgres-password>
    POSTGRES_DB=<your-postgres-database>
    ```
3. Run the following command to start the application:
    ```bash
     docker-compose up
    ```

4. Navigate to `http://localhost:8000/` in your web browser to access the phonebook application.

## Usage

- To create a new contact, send post request to `http://localhost:8000/contacts-api/` with the required fields.
- To view a list of all contacts, send get request `http://localhost:8000/contacts/`.
- To view a contact details, send get request `http://localhost:8000/contacts/<contact-id>`.
