from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['companyDB']

# Access the collections
employees_collection = db['Employees']
kpis_collection = db['KPIs']
performance_records_collection = db['Performance Records']
feedback_collection = db['Feedback']
goals_collection = db['Goals']
automated_reviews_collection = db['Automated Reviews']
dashboard_metrics_collection = db['Dashboard Metrics']

# Route for the home page to display employees
@app.route('/')
def index():
    employees = list(employees_collection.find())
    return render_template('index.html', employees=employees)

# Route to display KPIs
@app.route('/kpis')
def display_kpis():
    kpis = list(kpis_collection.find())
    return render_template('kpis.html', kpis=kpis)

# Route to display Performance Records
@app.route('/performance-records')
def display_performance_records():
    performance_records = list(performance_records_collection.find())
    return render_template('performance_records.html', performance_records=performance_records)

# Route to display Feedback
@app.route('/feedback')
def display_feedback():
    feedbacks = list(feedback_collection.find())
    return render_template('feedback.html', feedbacks=feedbacks)

# Route to display Goals
@app.route('/goals')
def display_goals():
    goals = list(goals_collection.find())
    return render_template('goals.html', goals=goals)

# Route to display Automated Reviews
@app.route('/automated-reviews')
def display_automated_reviews():
    automated_reviews = list(automated_reviews_collection.find())
    return render_template('automated_reviews.html', automated_reviews=automated_reviews)

# Route to display Dashboard Metrics
@app.route('/dashboard-metrics')
def display_dashboard_metrics():
    dashboard_metrics = list(dashboard_metrics_collection.find())
    return render_template('dashboard_metrics.html', dashboard_metrics=dashboard_metrics)

# New route to display everything on one page (Dashboard)
@app.route('/dashboard')
def dashboard():
    # Fetch data from MongoDB collections
    employees = list(employees_collection.find())
    kpis = list(kpis_collection.find())
    performance_records = list(performance_records_collection.find())
    feedbacks = list(feedback_collection.find())
    goals = list(goals_collection.find())
    automated_reviews = list(automated_reviews_collection.find())
    dashboard_metrics = list(dashboard_metrics_collection.find())
    
    # Pass all data to the dashboard.html template
    return render_template('dashboard.html', 
                           employees=employees,
                           kpis=kpis,
                           performance_records=performance_records,
                           feedbacks=feedbacks,
                           goals=goals,
                           automated_reviews=automated_reviews,
                           dashboard_metrics=dashboard_metrics)

if __name__ == '__main__':
    app.run(debug=True)
