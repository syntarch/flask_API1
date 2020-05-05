import json
from models import db, Volunteer, Street, District
from app import app

with open('districs.json', 'r', encoding='utf-8') as f:
    districts_list = f.read()
districts = json.loads(districts_list)


with app.app_context():
    for district in districts.values():
        districts_title = district['title']
        new_district = District(title=districts_title)
        for street_id in district['streets']:
            street = db.session.query(Street).get(street_id)
            new_district.streets.append(street)
            db.session.add(new_district)
    db.session.commit()


