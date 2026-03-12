from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

DATA_FILE = "alumni.json"

def load_alumni():
    with open(DATA_FILE) as f:
        return json.load(f)

def save_alumni(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# simulasi pencarian linkedin
def search_linkedin(name):
    companies = ["Google", "Tokopedia", "Shopee", "Telkom", "Gojek"]
    jobs = ["Software Engineer", "Data Analyst", "UI Designer", "Researcher"]

    return {
        "platform": "LinkedIn",
        "company": random.choice(companies),
        "position": random.choice(jobs),
        "location": "Indonesia"
    }

def search_scholar(name):
    return {
        "platform": "Google Scholar",
        "publication": "Machine Learning Research",
        "institution": "Universitas Indonesia"
    }

@app.route("/")
def index():
    alumni = load_alumni()
    return render_template("index.html", alumni=alumni)

@app.route("/search", methods=["POST"])
def search():
    name = request.json["name"]

    result = {
        "name": name,
        "linkedin": search_linkedin(name),
        "scholar": search_scholar(name),
        "status": "VALID"
    }

    return jsonify(result)

@app.route("/add_alumni", methods=["POST"])
def add_alumni():

    data = request.json

    alumni = load_alumni()

    new_alumni = {
        "nama": data["nama"],
        "tahun_lulus": data["tahun_lulus"],
        "program_studi": data["program_studi"],
        "email": data["email"],
        "kota": data["kota"]
    }

    alumni.append(new_alumni)

    save_alumni(alumni)

    return jsonify({"message":"Alumni berhasil ditambahkan"})

if __name__ == "__main__":
    app.run(debug=True)