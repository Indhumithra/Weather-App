
# 🌦 Weather App (Python Flask Project) 
live :http://127.0.0.1:5000

## 📌 Overview

The **Weather App** is a Python-based web application developed using the **Flask framework** and the **OpenWeather API**.
It allows users to search for any city in the world and view **live weather information** along with a **5-day weather forecast** through a clean and user-friendly interface.

This project demonstrates how to integrate third-party APIs with Python, handle dynamic data rendering, and design a visually appealing web application using HTML and CSS.

---

## 🎯 Objectives

* To build a real-time weather application using Python
* To understand API integration and JSON data handling
* To learn Flask routing and template rendering
* To create a responsive and attractive UI
* To implement proper error handling

---

## ✨ Features

* 🌍 Search weather for **any city worldwide**
* 🌡 Displays **current temperature**
* ☁ Shows **weather condition description**
* 💨 Displays **wind speed**
* 📅 Shows **5-day weather forecast**
* ❌ Custom error page for invalid city names
* 🎨 Attractive UI with background images

---

## 🛠 Technologies Used

* **Python 3**
* **Flask**
* **HTML5**
* **CSS3**
* **OpenWeather API**

---

## 📁 Project Structure

```
weather-app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── style.css
│   ├── Home page weather.png
│   ├── cast image.png
│   └── error.png
│
└── templates/
    ├── home.html
    ├── weather.html
    └── error.html
```

---

## 🔑 API Configuration

This project uses the **OpenWeather API**.

### Steps to get API key:

1. Visit [https://openweathermap.org](https://openweathermap.org)
2. Create a free account
3. Generate an API key
4. Add the key to `app.py` (or use `.env` file)

```python
API_KEY = "your_api_key_here"
```

⚠️ **Do not share your API key publicly**

---

## ▶ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Indhumithra/weather-app.git
cd weather-app
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🚫 Error Handling

* If the user enters an invalid city name, a **custom error page** is displayed.
* Network and API-related issues are handled gracefully.

---

## 📚 Learning Outcomes

* API integration using Python
* Flask application structure
* Jinja2 template rendering
* Frontend and backend integration
* GitHub project management

---

## 🚀 Future Enhancements

* Add weather icons (sun, rain, clouds)
* Auto-detect user location
* Dynamic background based on weather
* Mobile responsiveness
* Deploy on cloud platforms (Render / Railway)

---

## 🧑‍💻 Author

Developed by **[Your Name]**

---

## 📜 License

This project is for **educational purposes**.

---
Got it 👍
Based on the **screens you shared**, here is a **clear explanation you can use for GitHub / project submission** describing the **Home page and Weather (Cast) page**.

---

## 📄 Application Pages Explanation

### 1️⃣ Home Page
<img width="1892" height="781" alt="Screenshot 2026-02-09 182307" src="https://github.com/user-attachments/assets/1ef8fe42-91b4-4b76-9e2b-0f10b309790c" />


The Home page is the entry point of the Weather App. It features an attractive cloud-themed background with a bold and clear **Weather** title. Users can enter any city name using the search box and click the **Search** button to fetch live weather data. The layout is simple, centered, and user-friendly.

---

### 2️⃣ Weather (Cast) Page
<img width="1717" height="803" alt="Screenshot 2026-02-09 182415" src="https://github.com/user-attachments/assets/aa575980-fae8-412f-bc74-f484468af14d" />


The Weather page displays detailed live weather information for the selected city. It shows:

* City name and country
* Current date
* Current temperature (°C)
* Weather condition (Clear sky, Clouds, etc.)
* Wind speed
* A **5-day weather forecast** displayed in cards

The page uses a visually appealing background image and bold typography for better readability.

---

### 3️⃣ Error Page (Handled Automatically)
<img width="1588" height="746" alt="Screenshot 2026-02-09 182444" src="https://github.com/user-attachments/assets/4609dc23-59ed-4d5a-858f-13ca7f2630f6" />


If a user enters an invalid city name, a custom error page is displayed with a **404-style message** informing the user that the city does not exist and providing an option to return and try again.

---
Live : http://127.0.0.1:5000

