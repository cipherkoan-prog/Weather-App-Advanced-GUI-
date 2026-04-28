import json
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError
import tkinter as tk
from tkinter import messagebox
import threading

api_key="5e982487c5cdef23694bac24268fa161"

FILE_NAME="recent.json"

def load_recent():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []
    
def save_recent(city):
    data=load_recent()

    if city not in data:
        data.append(city)

    # keep only last 5 searches
    data=data[-5:]

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def start_search():
    loading_label.config(text="⏳ Loading...")
    weather_label.config(text="")

    # run background thread
    thread=threading.Thread(target=search_weather)
    thread.start()

def get_weather_data(city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response=requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()

    except Timeout:
        return {"error": "timeout"}

    except ConnectionError:
        return {"error": "no_internet"}

    except RequestException:
        return {"error": "api_fail"}
    

def format_weather_data(city, data):
    main=data["main"]
    weather=data["weather"] [0]
    wind=data["wind"]

    temperature=main["temp"]
    feels_like=main["feels_like"] 
    humidity=main["humidity"]
    windspeed=wind["speed"]
    description=weather["description"]

    result = (
        f"📍City: {city}\n"
        f"🌡Temperature: {temperature}°C\n"
        f"🤒Feels Like: {feels_like}°C\n"
        f"💧Humidity: {humidity}%\n"
        f"💨Wind Speed: {windspeed} m/s\n"
        f"☁Condition: {description}"
    )
    return result

def search_weather():
    city=city_entry.get().strip().title()

    if city == "":
        root.after(0, lambda: messagebox.showerror("Error", "Please enter a city name!"))
        root.after(0, lambda: loading_label.config(text=""))
        return

    data=get_weather_data(city)

    # Handle custom errors
    if "error" in data:
        def show_error():
            if data["error"] == "timeout":
                messagebox.showerror("Error", "Request timed out. Try again.")
            elif data["error"] == "no_internet":
                messagebox.showerror("Error", "No internet connection!")
            else:
                messagebox.showerror("Error", "API error occurred!")

            loading_label.config(text="")

        root.after(0, show_error)
        return

    # City not found
    if data.get("cod") == "404":
        root.after(0, lambda: messagebox.showerror("Error", "City not found!"))
        root.after(0, lambda: loading_label.config(text=""))
        return

    # Success
    result = format_weather_data(city, data)

    def update_ui():
        weather_label.config(text=result)
        loading_label.config(text="")
        save_recent(city)
        update_recent_list()

    root.after(0, update_ui)

   

def update_recent_list():
    recent_listbox.delete(0, tk.END)
    for city in load_recent():
        recent_listbox.insert(tk.END, city)

def on_recent_click(event):
    if not recent_listbox.curselection():
        return
    selected_city=recent_listbox.get(recent_listbox.curselection())
    city_entry.delete(0, tk.END)
    city_entry.insert(0, selected_city)

# GUI
root=tk.Tk()
root.title("Weather app")
root.geometry("400x450")
root.config(bg="#1e1e2f") # dark background

# Title Frame
title_frame=tk.Frame(root, bg="#1e1e2f")
title_frame.pack(pady=10)

title_label=tk.Label(
    title_frame,
    text="Weather App",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title_label.pack()

# Input Frame
input_frame=tk.Frame(root, bg="#1e1e2f")
input_frame.pack(pady=10)

city_entry=tk.Entry(
    input_frame,
    font=("Arial", 14),
    width=20,
    justify="center"
)
city_entry.pack(pady=5)

search_btn=tk.Button(
    input_frame,
    text="Search",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=start_search
)
search_btn.pack(pady=5)

# Result Frame
result_frame=tk.Frame(root, bg="#1e1e2f")
result_frame.pack(pady=1)

loading_label=tk.Label(
    result_frame,
    text="",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#1e1e2f"
)
loading_label.pack()

weather_label=tk.Label(
    result_frame,
    text="",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e2f",
    justify="left"
)
weather_label.pack(pady=5)

# Recent Searches Frame
recent_frame=tk.Frame(root, bg="#1e1e2f")
recent_frame.pack(pady=10)

tk.Label(
    recent_frame,
    text="Recent Searches",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#1e1e2f"
).pack()

recent_listbox=tk.Listbox(
    recent_frame,
    width=25,
    height=5,
    font=("Arial", 11)
)
recent_listbox.pack(pady=5)

recent_listbox.bind("<<ListboxSelect>>", on_recent_click)

update_recent_list()

root.mainloop()

