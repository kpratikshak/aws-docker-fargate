# Deploying a Dockerized Fargate App on AWS

A fully-deployed Flask application running on **AWS ECS Fargate**, featuring **real-time CloudWatch monitoring** and interactive UI with animated quotes.

---

## **Project Overview**

This project demonstrates:

- Deploying a Flask application in **Docker containers** on **AWS ECS Fargate**.
- Integrating **CloudWatch metrics** for monitoring CPU, memory, and container health.
- Using **Docker, ECR, and Fargate** for scalable, serverless container deployment.
- Implementing a **professional UI** with animations, step-by-step functionality, and a watermark.

---


## **Installation & Running Locally**

1. **Clone the repository:**
```bash
git clone https://github.com/Imash24/ECS-FLASK-APP/
cd ECS-FLASK-APP


2. Create Python Virtual Environment.
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt


4. Run the Flask App locally.
python app.py

**Docker Deployment**
1. Build Docker image:
docker build -t ecs-flask-app .

2. Run the container locally
docker run -p 5000:5000 ecs-flask-app
