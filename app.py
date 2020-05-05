from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import Config
from models import db, Volunteer, Street, District


app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app)
db.init_app(app)
migrate = Migrate(app, db)

admin.add_view(ModelView(Volunteer, db.session))
admin.add_view(ModelView(Street, db.session))
admin.add_view(ModelView(District, db.session))


@app.route('/districts/', methods=['GET'])
def index():
    districts_db = db.session.query(District).all()
    districts_list = [{'id': district.id, 'title': district.title} for district in districts_db]
    return jsonify(districts_list)

if __name__ == '__main__':
    app.run()
