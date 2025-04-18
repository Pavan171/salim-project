from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Use environment variables from ConfigMap and Secret
db_user = os.environ.get("POSTGRES_USER", "postgres")
db_pass = os.environ.get("POSTGRES_PASSWORD", "postgres")
db_host = os.environ.get("POSTGRES_HOST", "postgres-service.postgres.svc.cluster.local")
db_name = os.environ.get("POSTGRES_DB", "moviedb")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    movie = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    movie = request.form['movie']
    if not name or not movie:
        return "Both fields are required!", 400
    review = Review(name=name, movie=movie)
    db.session.add(review)
    db.session.commit()
    return render_template('result.html', name=name, movie=movie)

@app.route('/reviews')
def reviews():
    all_reviews = Review.query.all()
    return render_template('reviews.html', reviews=all_reviews)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
