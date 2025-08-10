from flask import Flask
from app.jobseeker.routes import jobseeker_bp

app = Flask(__name__)
app.register_blueprint(jobseeker_bp)

if __name__ == '__main__':
    app.run(debug=True)