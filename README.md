# Flask & PostgreSQL Docker Project

## Project Overview

This project containerizes a simple **Flask web application** that connects to a **PostgreSQL database**, using **Docker Compose** to manage both services efficiently.

### **🔹 Features**

- A **Flask web server** that responds with `Hello, Akshat Sahuji & 2022BCD0033`.
- A **PostgreSQL database service**.
- Environment variables for easy configuration.
- Uses **Docker Compose** for orchestration.
- Persistent **database storage** using Docker volumes.

---

##  Project Structure

```
D:\DEVops\Flask_App
│── Dockerfile                 # Docker build file for the Flask app
│── docker-compose.yml         # Defines Flask and PostgreSQL services
│── app.py                     # Flask application
│── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Getting Started

### **1.Prerequisites**

Ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### **2. Clone the Repository**

```sh
git clone https://github.com/akshatt123/Flask_App
cd Flask_App
```

### **3. Build and Run the Containers**

```sh
docker-compose up --build -d
```

This will:

- Build the **Flask app** (`web` service)
- Start the **PostgreSQL database** (`db` service)
- Map Flask's **port 5000** and PostgreSQL's **port 5432** to the host

### **4.Verify Running Containers**

```sh
docker ps
```

You should see **two containers** running (`flask_web` and `flask_db`).

### **5.Access the Web Application**

Open your browser and visit:

```
http://localhost:5000
```

Expected output:

```
Hello, Akshat Sahuji & 2022BCD0033
```

|   |
| - |

---

## Stopping & Removing Containers

To **stop** the running containers:

```sh
docker-compose down
```

To **remove everything** (including database data):

```sh
docker-compose down -v
```

---

##

