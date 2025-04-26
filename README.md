# Health Information System

A web application to manage client health data, enroll them in health programs, and provide APIs for external systems to access client profiles.

## Features

1. **Create Health Programs**  
   Administrators can create health programs such as TB, Malaria, HIV, etc.

2. **Register Clients**  
   Register new clients into the system with personal details.

3. **Enroll Clients in Programs**  
   Enroll clients into one or more health programs based on their needs.

4. **Search for Clients**  
   Search through a list of registered clients by their name or other identifiers.

5. **View Client Profiles**  
   View detailed profiles of clients, including personal information and enrolled programs.

6. **Expose Client Profiles via API**  
   The system provides an API endpoint to expose client profiles, allowing other systems to retrieve client information securely.

## Technologies Used

- **Backend:** Flask
- **Frontend:** JavaScript (Vanilla JS), HTML, CSS
- **Database:** [( PostgreSQL)]
- **Authentication:** JWT (JSON Web Token)
- **Deployment:** Vercel

## API Endpoints

### 1. **Create Health Program**
   - **Route:** `/api/create-program`
   - **Method:** `POST`
   - **Body:** `{ "name": "Program Name", "description": "Program Description" }`

### 2. **Register Client**
   - **Route:** `/api/register-client`
   - **Method:** `POST`
   - **Body:** `{ "client_name": "Client Name", "age": 30, "gender": "Male" }`

### 3. **Enroll Client in Program**
   - **Route:** `/api/enroll-client`
   - **Method:** `POST`
   - **Body:** `{ "client_id": 1, "program_id": 2 }`

### 4. **Search for Client**
   - **Route:** `/api/search-client?client_name=Jane`
   - **Method:** `GET`
   - **Response:** Returns details of the client, including enrolled programs.

### 5. **View Client Profile**
   - **Route:** `/api/view-client-profile?client_id=1`
   - **Method:** `GET`
   - **Response:** Detailed profile of the client.

### 6. **Expose Client Profile via API**
   - **Route:** `/api/client-profile`
   - **Method:** `GET`
   - **Authentication:** JWT
   - **Response:** Returns a client's profile data, including enrolled programs.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/health-information-system.git

2. Navigate into the project directory
   ```bash
    cd health-information-system
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application
   ```bash
   flask run

   

