# 🚗 AutoSage  
## Multimodal AI Vehicle Intelligence System  

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_2.5_Flash-orange)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

AutoSage is a **multimodal AI-powered automotive intelligence system** built using **Google Gemini 2.5 Flash**.  
The application provides structured vehicle insights from images and supports automotive advisory queries via a domain-restricted AI assistant.

Developed as part of a **Google Cloud – Generative AI Internship**, this project demonstrates real-world implementation of:

- Multimodal AI integration  
- Prompt engineering  
- Secure API handling  
- Domain restriction logic  
- Real-time Streamlit deployment  

---

## 📌 Problem Statement

Modern vehicle buyers often face challenges in:

- Identifying vehicle models from images  
- Understanding technical specifications clearly  
- Comparing maintenance and resale value  
- Selecting eco-friendly vehicle options  
- Making informed purchasing decisions  

There is a need for a structured, AI-driven automotive intelligence assistant that simplifies vehicle decision-making.

---

## 🎯 Project Objectives

- Implement image-based vehicle recognition using Gemini multimodal capabilities  
- Generate structured automotive insights  
- Restrict chatbot responses strictly to automotive domain  
- Provide budget-based and comparison-based recommendations  
- Deploy as a real-time interactive web application  

---

## 🔍 Core Modules

### 1️⃣ Image-Based Vehicle Analysis Module

Users upload a vehicle image and receive structured insights including:

- Brand & Model Identification  
- Launch Year  
- Vehicle & Fuel Type  
- Engine & Performance Specifications  
- Mileage & Price Range (INR)  
- Maintenance Level  
- Safety Features  
- Target Audience  
- Estimated 10-Year Resale Value  
- Market Positioning Summary  

Structured prompt engineering ensures consistent formatting and professional output generation.

---

### 2️⃣ Automotive AI Advisory Assistant

The text-based assistant supports:

- Budget-based vehicle recommendations  
- Model comparisons  
- EV & Hybrid suggestions  
- Seasonal maintenance advice  
- Simplified explanation of technical terms  

The assistant is **domain-restricted**, ensuring it only responds to automotive-related queries.

---

## ⚙️ Why Gemini 2.5 Flash?

Gemini 2.5 Flash was selected due to:

- Fast multimodal processing  
- Low latency inference  
- Cost-efficient API usage  
- Strong structured response generation  
- Reliable image + text understanding  

---

## 🏗 System Architecture

```text
User Input (Image / Text)
        ↓
Streamlit Frontend
        ↓
Prompt Engineering Layer
        ↓
Gemini 2.5 Flash API
        ↓
Structured Insight Engine
        ↓
Formatted Response Display
```

---

## 🛠 Technology Stack

- Python  
- Streamlit  
- Google Gemini 2.5 Flash API  
- Prompt Engineering  
- Multimodal AI  
- python-dotenv (Secure API Management)  

---

## 🧪 Testing & Validation Strategy

The system was validated using:

- Image format validation (JPEG / PNG)  
- Non-vehicle image handling  
- Domain restriction enforcement  
- Conditional UI rendering tests  
- Structured output consistency checks  
- API error handling validation  

---

## 📸 Application Screenshots

### 🏠 Home Interface
![Home Screen](assets/home.png)

---

## 🚗 Four-Wheeler Analysis

### 📷 Analysis Output – Part 1
![Four Wheeler 1](assets/four_Wheeler_image_analysis/image1.jpg)

### 📊 Analysis Output – Part 2
![Four Wheeler 2](assets/four_Wheeler_image_analysis/image2.jpg)

### 📈 Analysis Output – Part 3
![Four Wheeler 3](assets/four_Wheeler_image_analysis/image3.jpg)

---

## 🏍 Two-Wheeler Analysis

### 📷 Analysis Output – Part 1
![Two Wheeler 1](assets/two_wheeler_image_analysis/image1.jpg)

### 📊 Analysis Output – Part 2
![Two Wheeler 2](assets/two_wheeler_image_analysis/image2.jpg)


---

## 🤖 Automotive AI Assistant
![Chatbot](assets/chatbot.png)

---

## 🚀 Live Deployment

🔗 **Streamlit App:**  
https://autosage-app-gp4curmwapppp2edzadnwdta.streamlit.app/

---

## 🎥 Project Demonstration

🔗 **Demo Video:**  
https://drive.google.com/file/d/1rrwIvtJkw4qBJb4GAjfqua2YbGsxRw4e/view?usp=drive_link

---

## 📂 Project Structure

```text
autoexpert/
│
├── app.py
├── requirements.txt
├── README.md
├── .env                      # Environment variables (not pushed to GitHub)
│
├── images/                   # Test images used for validation
│   ├── image1.png
│   ├── image2.png
│   ├── image3.png
│   └── ...
│
├── assets/                   # Screenshots for README
│   │
│   ├── home.png
│   ├── chatbot.png
│   │
│   ├── four_wheeler_analysis/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── image3.jpg
│   │
│   └── two_wheeler_analysis/
│       ├── image1.jpg
│       └── image2.jpg
│
└── docs/
    └── AutoSage_Project_Report.pdf
```
---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/eedaratejaswini-07/autoexpert.git
cd autoexpert
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

⚠️ Make sure `.env` is added to `.gitignore`.

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## ⚠️ Limitations

- Dependent on Gemini API quota limits  
- AI-based estimations may vary slightly  
- Requires stable internet connectivity  
- Image recognition accuracy depends on clarity and angle  

---

## 🔮 Future Enhancements

- VIN-based vehicle identification  
- Integration with real-time automotive databases  
- Voice-enabled assistant  
- Personalized AI recommendations  
- Cloud scalability & containerization  

---

## 📘 Documentation

Detailed technical documentation available in:

```
docs/AutoSage_Project_Report.pdf
```

---

## 👩‍💻 Developers

**Eedara Tejaswini**  
**Prasanna Kumar Raparla**  
**Sai Kumar Ramoju**  
**Sandeep Peruri**  

Google Cloud – Generative AI Internship  

---

## 📜 License

This project is developed for educational and internship purposes only.
