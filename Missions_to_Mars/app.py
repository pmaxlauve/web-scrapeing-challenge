from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape2

# Create an instance of Flask
app = Flask(__name__)


# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/m2m")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    m2m_data = mongo.db.m2m_vars.find_one()



    # Return template and data
    return render_template("index.html", m2m=m2m_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():

    
    mars_data = scrape2.scrape_data()
    mongo.db.m2m_vars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

    










if __name__ == "__main__":
    app.run(debug=True)