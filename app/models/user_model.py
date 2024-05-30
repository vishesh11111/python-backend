# app/models/user_model.py
from app import db
from sqlalchemy import JSON

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    organization = db.Column(db.String(100))
    title = db.Column(db.String(100))
    address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    membership_level = db.Column(db.String(100))
    profile_url = db.Column(db.String(100))
    zip_code = db.Column(db.Integer)
    business_phone = db.Column(db.String(100))
    mobile_number = db.Column(db.String(100))
    registration_date = db.Column(db.DateTime)
    interested = db.Column(db.Boolean)
    membership = db.Column(db.String(100))
    access_role = db.Column(db.String(100))
    membership_plan_id = db.Column(db.String(100))
    access_page = db.Column(JSON)
    photos = db.Column(JSON)
    last_login = db.Column(db.DateTime)
    time_zone = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=True)
    access_level = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
