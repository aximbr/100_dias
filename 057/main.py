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

@app.route('/guess/<name_in>')
def great(name_in):
    name = str(name_in).title()
    age = get_age(name)
    gender = get_gender(name)
    return render_template("guess.html", out_name = name, out_age = age, out_gender = gender, year = current_year, )

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


