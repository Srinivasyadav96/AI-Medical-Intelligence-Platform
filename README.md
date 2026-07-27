# Advanced AI Medical Intelligence Platform

An end-to-end AI-powered web application for automated chest X-ray disease detection, Explainable AI visualization, AI-assisted medical report generation, and prediction history management.

------

# Project Overview

The Advanced AI Medical Intelligence Platform is a Django-based web application that leverages Deep Learning, Explainable AI (Grad-CAM), and Large Language Models (LLMs) to analyze chest X-ray images.

The application enables users to upload a chest X-ray image, predicts whether the patient has **Pneumonia** or is **Normal**, explains the prediction using Grad-CAM heatmaps, generates an AI-assisted medical report using the Groq LLM API, stores the prediction history in Neon PostgreSQL, and provides REST API endpoints.

------

#  Features

- Chest X-ray image upload
- Pneumonia Detection using TensorFlow/Keras
- Explainable AI (Grad-CAM)
- AI-assisted Medical Report Generation (Groq LLM)
- Prediction Confidence Score
- PostgreSQL(Neon) Database Integration
- Prediction History
- Django REST API { http://127.0.0.1:8000/api/predictions/ }
- Responsive Django Web Interface

---

#  Tech Stack

# Backend
- Python
- Django
- Django REST Framework

# Deep Learning
- TensorFlow
- Keras

# Explainable AI
- Grad-CAM

# AI
- Groq API (LLM)

# Database
- (Neon) PostgreSQL

## Frontend
- HTML
- CSS
- Bootstrap

## Other Tools

- NumPy
- Pillow
- Gunicorn
- WhiteNoise
- Git
- GitHub

---

#  Project Structure

```
AI-Medical-Intelligence-Platform/
│
├── medical_ai/
│
├── predictor/
│
├── ml/
│   └── model.keras
│
|--notebook/{dataset analysis, preprocessing, training model}
├── templates/
│
├── static/
│
├── media/
│
├── requirements.txt
│
├── manage.py
│
└── README.md
```

---

#  System Workflow

```
Chest X-ray Image
        │
        ▼
Image Upload
        │
        ▼
Image Preprocessing
        │
        ▼
TensorFlow Model
        │
        ▼
Prediction
        │
        ├──────────────► Confidence Score
        │
        ├──────────────► Grad-CAM Heatmap
        │
        ├──────────────► Groq AI Medical Report
        │
        ▼
Store in PostgreSQL
        │
        ▼
Prediction History
        │
        ▼
REST API
```

---

#  Deep Learning Model

Model Used:

- TensorFlow/Keras CNN Model

Dataset:

- Chest X-Ray (Pneumonia)

Output Classes

- NORMAL
- PNEUMONIA

Image Size

- 224 × 224

---

# Explainable AI

Grad-CAM is used to visualize which regions of the chest X-ray influenced the model's prediction.

This helps improve model transparency and interpretability for medical professionals.

---

#  AI Medical Report

After prediction, the application sends the prediction details to the Groq Large Language Model to generate an AI-assisted medical report containing:

- Disease Summary
- Possible Findings
- Clinical Interpretation
- Suggested Medical Advice

---

#  Database

Prediction history is stored in PostgreSQL.

Each record contains:

- Uploaded Image
- Prediction
- Confidence Score
- Generated Medical Report
- Timestamp

---

#  REST API

Example Endpoint

```
GET /api/history/ { http://127.0.0.1:8000/api/predictions/ }
```

Returns prediction history in JSON format.

---

#  Screenshots

## Home Page

<img width="1920" height="1080" alt="homepage_screenshot" src="https://github.com/user-attachments/assets/09cb0281-4573-4df4-ab72-a765b8a31dcc" />





---

## Prediction Result
{picture_1}
<img width="1920" height="1080" alt="prediction_result_screenshot1" src="https://github.com/user-attachments/assets/a0c5c618-ceee-40d6-b60b-84f7d5689fdb" />

{picture_2}
<img width="1920" height="1080" alt="result_screenshot_2" src="https://github.com/user-attachments/assets/8adefe27-08f5-46db-8128-8a88087ff542" />


---

## Prediction History

<img width="1920" height="1080" alt="history_screenshot" src="https://github.com/user-attachments/assets/28ce3cf6-8939-46a1-abec-d7133b125474" />


---

#  Installation

Clone the repository

```bash
git clone https://github.com/Srinivasyadav96/AI-Medical-Intelligence-Platform.git
```

Move into project

```bash
cd AI-Medical-Intelligence-Platform
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Start server

```bash
python manage.py runserver
```

---

#  Requirements

Install all dependencies

```bash
pip install -r requirements.txt
```

---

#  Deployment

Deployment configuration was prepared using:

- Gunicorn
- WhiteNoise
- PostgreSQL

Live deployment is not included in this submission.

---

# 📈 Future Improvements

- Multi-Disease Detection
- Doctor Authentication
- PDF Report Export
- Patient Dashboard
- Appointment Integration
- Cloud Deployment
- Docker Support
- Model Optimization

---

#  Author

**M. Srinivas**

GitHub:

https://github.com/Srinivasyadav96

---

#  License

This project was developed as part of the AI/ML Engineer Technical Assessment and is intended for educational and evaluation purposes.

---

##  Acknowledgement

This project was developed to demonstrate practical knowledge of:

- Deep Learning
- Explainable AI (XAI)
- Large Language Models
- Django Web Development
- REST APIs
- PostgreSQL
- AI Application Development
