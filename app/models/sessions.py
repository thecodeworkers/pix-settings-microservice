from mongoengine import Document, StringField, BooleanField


class Sessions(Document):
	user = StringField(required=True)
	app = StringField(max_length=100, required=True)
	ip = StringField(required=True)
	location = StringField(required=True)
	userAgent = StringField(required=True)
	valid = BooleanField(required=True)
	active = BooleanField(required=True)

