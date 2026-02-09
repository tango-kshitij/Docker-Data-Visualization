# Dockerized Data Visualization Dashboard

An interactive data visualization dashboard built using Python and Streamlit, fully containerized using Docker to ensure platform-independent deployment.

---

## Project Overview

This project demonstrates how data visualization applications can be packaged and deployed using Docker. The dashboard reads data from a CSV file, displays it in tabular form, and generates visual insights using charts. Docker ensures that the application runs consistently across different systems without dependency issues.

---

## Objectives

- To analyze and visualize structured data
- To build an interactive dashboard using Python
- To containerize the application using Docker
- To enable easy, one-command deployment
- To demonstrate basic DevOps and containerization concepts

---

## Technologies Used

- **Programming Language:** Python  
- **Data Processing:** Pandas  
- **Data Visualization:** Matplotlib  
- **Dashboard Framework:** Streamlit  
- **Containerization:** Docker  
- **Dataset Format:** CSV  

---

## Project Structure
```
docker-dashboard/
│
├── app.py # Main application file
├── data.csv # Sample dataset
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
└── README.md # Project documentation
```

---

## Features

- Displays raw dataset in tabular form
- Visualizes data using:
  - Line chart
  - Bar chart
  - Pie chart
- Interactive web-based dashboard
- Fully containerized application
- Platform-independent execution

---

## How to Run the Project

### 1. Prerequisites
- Docker installed on your system  
- Internet connection (for initial image build)
- Verify Docker installation:
```
bash
docker --version
```

---

### 2. Clone the repository
```
git clone https://github.com/your-username/dockerized-data-visualization-dashboard.git
cd dockerized-data-visualization-dashboard
```

---

### 3. Build the Docker image
```
docker build -t data-dashboard .
```

---

### 4. Run the Docker Container
```
docker run -p 8501:8501 data-dashboard
```

---

### 5. Access the Dashboard
```
http://localhost:8501
```

---

## How It Works
The dataset (data.csv) is loaded using Pandas
Streamlit provides a web-based dashboard interface
Matplotlib generates visualizations
Docker packages the application and dependencies
The container runs the dashboard consistently on any system

---

## Expected Output
A web dashboard displaying the dataset
Visual graphs representing data trends and distributions
Docker container running the application successfully

---

## Applications
Academic data analysis projects
Business and sales analytics
Environmental and weather data analysis
Learning Docker and DevOps basics

---

## Future Enhancements
Real-time data integration
Cloud deployment
Advanced interactive charts
User authentication
Database integration

---

## Conclusion
This project successfully integrates data visualization with containerization technology. By using Docker, the application becomes portable, scalable, and easy to deploy, addressing common challenges in traditional software deployment. The project provides hands-on experience with Python, data visualization, and DevOps concepts.

---

## Author
Kshitij Gupta
CSE / Manipal University Jaipur
GitHub: https://github.com/tango-kshitij