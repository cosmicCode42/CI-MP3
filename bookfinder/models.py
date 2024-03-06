from bookfinder import db


class Author(db.Model):
    # schema for the Author model
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(75), unique=True, nullable=False)
    books = db.relationship("Book", backref="author", cascade="all, delete", lazy=True)

    def __repr__(self):
        # represents self in the form of a string
        return self.author_name


class Genre(db.Model):
    #schema for the Genre model
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.genre_name


class Book(db.Model):
    # schema for the Book model
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(125), unique=True, nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete="CASCADE"), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return self.book_name
