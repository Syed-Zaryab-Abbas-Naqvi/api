from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

# In-memory database to store tasks (simple list)
tasks = []

# Replace this with your actual OpenWeatherMap API Key
WEATHER_API_KEY = "5959144c3cde46931596b819ab966fd9"

# Home route to display the weather and tasks
@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            weather_data = get_weather(city)
    
    return render_template("weather.html", weather_data=weather_data, tasks=tasks, enumerate=enumerate)


# Function to get weather data from OpenWeatherMap API
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# API to add a task
@app.route("/add", methods=["POST"])
def add_task():
    task_content = request.form.get("task")
    if task_content:
        tasks.append(task_content)
    return redirect(url_for("home"))

# API to delete a task by index
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("home"))

# API to retrieve tasks (for potential AJAX use)
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
