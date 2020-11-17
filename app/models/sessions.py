from mongoengine import Document, StringField, BooleanField, ObjectIdField


class Sessions(Document):
	user = ObjectIdField(required=True)
	app = StringField(max_length=100, required=True)
	ip = StringField(required=True)
	location = StringField(required=True)
	userAgent = StringField(required=True)
	valid = BooleanField(required=True)
	active = BooleanField(required=True)
