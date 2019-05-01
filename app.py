# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import os

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"]="mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    mars_mission = mongo.db.mars_mission.find_one()

    # return template and data
    return render_template("index.html", mars_mission=mars_mission)


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions  
    mars_mission = mongo.db.mars_mission
    #mars_data = scrape_mars.scrape_mars_news()
    #mars_data = scrape_mars.scrape_mars_image()
    #mars_data = scrape_mars.scrape_mars_weather()
    #mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_hemisphers()
    print(mars_data)
    
    mars_mission.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
