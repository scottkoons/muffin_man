"""Model for cupcakes"""

from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://tinyurl.com/demo-cupcake"

db = SQLAlchemy()


class Cupcake(db.Model):
    """Cupcake Object."""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=GENERIC_IMAGE)

    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.image or GENERIC_IMAGE

    def to_dict(self):
        """Create a dict with cupcake info gathered from form"""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }


def connect_db(app):
    """Connect this database to cupcake Flask app."""

    db.app = app
    db.init_app(app)
