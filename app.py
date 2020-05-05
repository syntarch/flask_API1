from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import Config
from models import db, Volunteer, Street, District, Request


app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app)
db.init_app(app)
migrate = Migrate(app, db)

admin.add_view(ModelView(Volunteer, db.session))
admin.add_view(ModelView(Street, db.session))
admin.add_view(ModelView(District, db.session))
admin.add_view(ModelView(Request, db.session))


@app.route('/districts/', methods=['GET'])
def index():
    districts_db = db.session.query(District).all()
    districts_list = [{'id': district.id, 'title': district.title} for district in districts_db]
    return jsonify(districts_list)


@app.route('/streets/', methods=['GET'])
def streets_f():
    district_id = request.args.get('district')
    district_db = db.session.query(District).get(district_id)
    streets_in_district = district_db.streets
    streets_list = [{'id': street.id, 'title': street.title,
                     'volunteers': [volunteer.id for volunteer in street.volunteers]}
                    for street in streets_in_district]
    return jsonify(streets_list)


@app.route('/volunteers/', methods=['GET'])
def volunteers_f():
    street_id = request.args.get('streets')
    street_db = db.session.query(Street).get(street_id)
    volunteers_on_street = street_db.volunteers
    volunteers_list = [{'id': volunteer.id, 'name': volunteer.name, 'userpic': volunteer.userpic, 'phone': volunteer.phone}
                       for volunteer in volunteers_on_street]
    return jsonify(volunteers_list)


@app.route('/helpme/', methods=['POST'])
def request_f():
    accepted_data = request.json
    new_request = Request(district=accepted_data.get('district'),
                          street=accepted_data.get('street'),
                          volunteer=accepted_data.get('volunteer'),
                          address=accepted_data.get('address'),
                          name=accepted_data.get('name'),
                          surname=accepted_data.get('surname'),
                          phone=accepted_data.get('phone'),
                          text=accepted_data.get('text'))
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run()
