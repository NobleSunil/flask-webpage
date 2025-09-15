from flask import Flask, render_template
import os  # Needed to read environment variables

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Use PORT from OpenShift if available, default to 8080
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port)
