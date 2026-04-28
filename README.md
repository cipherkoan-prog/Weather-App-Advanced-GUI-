# 🌤 Weather App (Advanced GUI)

A modern **Python Weather App** built using **Tkinter**, **OpenWeatherMap API**, and **JSON storage**.
This project demonstrates real-world development concepts like API integration, GUI design, threading, and error handling.

---

## 🚀 Features

* 🔍 Search weather by city
* 🌡 Shows:

  * Temperature
  * Feels Like
  * Humidity
  * Wind Speed
  * Weather Condition
* 🕒 Recent Searches (stored using JSON)
* ⚡ Loading Indicator (non-blocking UI using threading)
* ❌ Error Handling:

  * No internet connection
  * API failure
  * Invalid city
* 🎨 Clean GUI with:

  * Frames layout
  * Custom colors
  * Bigger fonts

---

## 🛠 Tech Stack

* Python 3
* Tkinter (GUI)
* Requests (API calls)
* JSON (data storage)
* Threading (for smooth UI)

---

## 📂 Project Structure

```
Weather-App/
│
├── with_gui.py        # Main application file
├── recent.json        # Stores recent searches
└── README.md          # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/weather-app.git
```

2. Navigate to project folder:

```
cd weather-app
```

3. Install required library:

```
pip install requests
```

---

## ▶️ Run the App

```
python with_gui.py
```

---

## 🔑 API Setup

This project uses the OpenWeatherMap API.

1. Go to: https://openweathermap.org/api
2. Create a free account
3. Get your API key
4. Replace in code:

```
api_key = "YOUR_API_KEY"
```

---

## 🧠 What I Learned

* API integration in Python
* Building GUI using Tkinter
* Using threading to prevent UI freezing
* Handling real-world errors (network, API)
* Storing and managing data using JSON
* Writing clean and structured code

---

## 📸 Screenshots (Optional)

*Add screenshots of your app here*

---

## 🚀 Future Improvements

* 🌤 Add weather icons
* 📍 Auto-detect location
* 📊 Show forecast (next 5 days)
* 🎨 Improve UI (modern design)
* 📦 Convert to .exe application

---

## 🤝 Contributing

Feel free to fork this project and improve it!

---

## 📜 License

This project is open-source and free to use.

