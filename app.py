from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("register"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        studentid = request.form.get("studentid", "").strip()

        if name and email and studentid and name == studentid:
            return render_template("success.html")

    return render_template("register.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)