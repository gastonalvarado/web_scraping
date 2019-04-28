from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn = "mongodb://localhost:27017"
client = PyMongo.MongoClient(conn)



# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


#@app.route("/")
#def index():
    #listings = mongo.db.listings.find_one()
    #return render_template("index.html", listings=listings)


@app.route("/scrape")
def scraper():
    #listings = mongo.db.listings
    listings_data = scrape_mars.scrape()
    #listings.update({}, listings_data, upsert=True)
    return render_template("index.html", listings=listings_data)


if __name__ == "__main__":
    app.run(debug=True)
