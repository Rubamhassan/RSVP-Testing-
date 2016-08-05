from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # this is a function that creates a game and adds it to the database.
    t2r = Game(name='Ticket to Ride', description='cross country adventure')
    pgrid = Game(name='Power Grid', description='supply with power')

    db.session.add_all([t2r, pgrid])
    db.session.commit()



if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."