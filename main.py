from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

# Database Model - Matches your exact schema
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    map_url = db.Column(db.String(500))  # URL to Google Maps
    img_url = db.Column(db.String(500))  # URL to cafe image
    location = db.Column(db.String(200), nullable=False)
    has_sockets = db.Column(db.Boolean, default=False)  # Power outlets
    has_toilet = db.Column(db.Boolean, default=False)
    has_wifi = db.Column(db.Boolean, default=False)
    can_take_calls = db.Column(db.Boolean, default=False)
    seats = db.Column(db.String(50))  # e.g., "20-30"
    coffee_price = db.Column(db.String(20))  # e.g., "₦1,500"

# Routes
@app.route('/')
def home():
    cafes = Cafe.query.all()
    return render_template('index.html', cafes=cafes)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    if request.method == 'POST':
        new_cafe = Cafe(
            name=request.form['name'],
            map_url=request.form.get('map_url', ''),  # Optional
            img_url=request.form.get('img_url', ''),  # Optional
            location=request.form['location'],
            has_sockets=bool(request.form.get('has_sockets')),
            has_toilet=bool(request.form.get('has_toilet')),
            has_wifi=bool(request.form.get('has_wifi')),
            can_take_calls=bool(request.form.get('can_take_calls')),
            seats=request.form.get('seats', 'Not specified'),
            coffee_price=request.form.get('coffee_price', 'Not listed')
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)