from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import random

app = Flask(__name__)
app.secret_key = "secret123"

DATA_FILE = "alumni.json"

# ================= DATA =================

def load_alumni():
    with open(DATA_FILE) as f:
        return json.load(f)

def save_alumni(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ================= LOGIN =================

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "123":
            session["login"] = True
            return redirect(url_for("index"))
        else:
            return "Login gagal"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("login", None)
    return redirect("/login")

# ================= HALAMAN UTAMA =================

@app.route("/")
def index():
    if not session.get("login"):
        return redirect("/login")
    return render_template("index.html")

# ================= GET ALUMNI (SEARCH + LIMIT) =================

@app.route("/get_alumni")
def get_alumni():
    if not session.get("login"):
        return jsonify({"error": "Unauthorized"}), 401

    keyword = request.args.get("keyword", "").lower()
    alumni = load_alumni()

    if keyword:
        alumni = [a for a in alumni if keyword in a["nama"].lower()]

    return jsonify(alumni[:20])  # limit 20 data

# ================= PELACAKAN =================

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
        "institution": "Universitas Muhammadiyah Malang"
    }

@app.route("/search", methods=["POST"])
def search():
    if not session.get("login"):
        return jsonify({"error": "Unauthorized"}), 401

    name = request.json["name"]

    result = {
        "name": name,
        "linkedin": search_linkedin(name),
        "scholar": search_scholar(name),
        "status": "VALID"
    }

    return jsonify(result)

# ================= TAMBAH ALUMNI =================

@app.route("/add_alumni", methods=["POST"])
def add_alumni():
    if not session.get("login"):
        return jsonify({"error": "Unauthorized"}), 401

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

    return jsonify({"message": "Alumni berhasil ditambahkan"})

# ================= RUN =================

if __name__ == "__main__":
    app.run(debug=True)
