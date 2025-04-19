from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration (Using SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Contact Model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Contact {self.name}>'

# Create the Database
with app.app_context():
    db.create_all()

# Define a Route for the Contact Form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        new_entry = Contact(name=data['name'], email=data['email'], message=data['message'])

        db.session.add(new_entry)
        db.session.commit()

        return "Message received!", 200

    return render_template('contact.html')  # Ensure you have a contact.html template

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
