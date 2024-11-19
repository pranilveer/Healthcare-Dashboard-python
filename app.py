from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        file = request.files.get('file')

        if not name or not age or not file:
            flash("All fields are required!", "error")
            return redirect(url_for('index'))

        print(f"Name: {name}, Age: {age}, File: {file.filename}")
        flash("Form submitted successfully!", "success")
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
