from mongoengine import Document, StringField, BooleanField, ObjectIdField


class Sessions(Document):
	user = ObjectIdField(required=True)
	app = StringField(min_length=2,max_length=100, required=True)
	ip = StringField(min_length=4,required=True)
	location = StringField(min_length=3,required=True)
	userAgent = StringField(min_length=2,required=True)
	valid = BooleanField(required=True)
	active = BooleanField(required=True)
