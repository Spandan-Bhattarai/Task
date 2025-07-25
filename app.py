from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description, "category": self.category}

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/blogs", methods=["GET"])
def get_all_blogs():
    blogs = Blog.query.all()
    return jsonify([blog.to_dict() for blog in blogs])

@app.route("/blogs/<int:id>", methods=["GET"])
def get_blog(id):
    blog = Blog.query.get_or_404(id)
    return jsonify(blog.to_dict())

@app.route("/blogs", methods=["POST"])
def create_blog():
    data = request.get_json()
    new_blog = Blog(title=data["title"], description=data["description"], category=data["category"])
    db.session.add(new_blog)
    db.session.commit()
    return jsonify(new_blog.to_dict()), 201

@app.route("/blogs/<int:id>", methods=["PUT"])
def update_blog(id):
    blog = Blog.query.get_or_404(id)
    data = request.get_json()
    blog.title = data.get("title", blog.title)
    blog.description = data.get("description", blog.description)
    blog.category = data.get("category", blog.category)
    db.session.commit()
    return jsonify(blog.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
