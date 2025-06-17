# Flask Backend Distributed System

This project is a distributed system built using Docker, Docker Compose, and multiple backend services. It provides a scalable backend architecture with dedicated services for authentication, user management, and product handling, all orchestrated within containers. The system also features a simple frontend built with HTML and JavaScript to interact with the backend services.

## Features

- **Microservices Architecture**: Each core function (AUTH, USERS, PRODUCTS) runs as an independent service.
- **Containerization**: All backend services are containerized using Docker and orchestrated with Docker Compose.
- **RESTful APIs**: Each backend service exposes RESTful endpoints for easy integration.
- **Frontend**: Simple HTML and JavaScript files for interacting with backend services.
- **Scalability**: Easily scale services by adjusting Docker Compose configuration.

## Services Overview

- **AUTH**: Handles authentication, login, and token management.
- **USERS**: Manages user data and profiles.
- **PRODUCTS**: Manages product catalog and related operations.
- **Frontend**: A set of standalone HTML and JavaScript files used to interact with the backend APIs.  
  **Note:** The frontend is not containerized. You must open the HTML files directly in your browser from your host machine.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CrisAti/flask_backend.git
   cd flask_backend
   ```

2. **Build and run the backend services using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Access the frontend:**
   - Open the `frontend` directory in your project.
   - Double-click the HTML file you want to use (e.g., `index.html`) to open it in your browser.
   - The frontend will make API calls to the backend services running in Docker.

### Stopping the Services

To stop and remove all running containers:
```bash
docker-compose down
```

## Usage

- The frontend HTML files provide basic forms and interfaces to interact with AUTH, USERS, and PRODUCTS services.
- You can also use tools like [Postman](https://www.postman.com/) or `curl` to test the REST APIs directly.

## Project Structure

```
flask_backend/
│
├── auth/           # Authentication service (Flask app)
├── users/          # User management service (Flask app)
├── products/       # Product management service (Flask app)
├── frontend/       # HTML and JavaScript frontend (not containerized)
├── docker-compose.yml
└── README.md
```

## Customization

- To add more services, create a new directory and add its configuration to `docker-compose.yml`.
- Update the frontend to call new APIs as needed.

## Contributing

Contributions are welcome! Please open issues or pull requests for improvements and fixes.

## License

This project is licensed under the MIT License.
