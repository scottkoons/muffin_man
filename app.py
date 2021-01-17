"""Flask app to show and store cupcake information"""

from flask import Flask, json, request, render_template, redirect, flash, jsonify
from models import db, connect_db, Cupcake
# from forms import

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SECRET_KEY'] = "usafa1993"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


# Render homepage with all cupcakes
@app.route('/')
def root():
    """Homepage ordered by flavor in ascending order"""
    cupcakes = Cupcake.query.order_by(Cupcake.flavor.asc()).all()
    return render_template("index.html", cupcakes=cupcakes)


# Send to add cupcake form
@app.route('/add')
def add_form():
    """Add Cupcake Form"""

    return render_template("add.html")


# Get JSON data for all cupcakes
@app.route("/api/cupcakes")
def list_cupcakes():
    """Returns json for all cupcakes in database."""
    all_cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return render_template("edit.html", cupcake=cupcake)
    # return jsonify(cupcake=cupcake.to_dict())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():

    data = request.json

    new_cupcake = Cupcake(flavor=data['flavor'],
                          rating=data['rating'],
                          size=data['size'],
                          image=data['image'] or None)

    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.to_dict()), 201)


@app.route("/api/cupcakes/<int:id>", methods=['PATCH'])
def update_cupcake(id):
    data = request.json

    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = data.get('flavor', cupcake.flavor)
    cupcake.rating = data.get('rating', cupcake.rating)
    cupcake.size = data.get('size', cupcake.size)
    cupcake.image = data.get('image', cupcake.image)

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:id>", methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(msg="Deleted")
