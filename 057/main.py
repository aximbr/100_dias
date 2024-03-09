from flask import Flask, render_template
import datetime
import requests

URL_AGE = "https://api.agify.io?name="
URL_GENDER = "https://api.genderize.io?name="

app = Flask(__name__)

current_year = datetime.datetime.now().year

def get_age(name):
    response = requests.get(URL_AGE+name)
    response.raise_for_status()

    if response.status_code == 200:
        return response.json()['age']
    
def get_gender(name):
    response = requests.get(URL_GENDER+name)
    response.raise_for_status()

    if response.status_code == 200:
        return response.json()['gender'] 
       
        
@app.route('/')
def home():
    return render_template("index.html", year = current_year)

@app.route('/<name_in>')
def great(name_in):
    name = str(name_in).capitalize()
    age = get_age(name)
    gender = get_gender(name)
    return render_template("index.html", out_name = name, out_age = age, out_gender = gender, year = current_year, )

if __name__ == "__main__":
    app.run(debug=True)


