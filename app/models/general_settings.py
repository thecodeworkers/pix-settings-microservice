from mongoengine import Document, StringField, IntField, BooleanField

class GeneralSettings(Document):
	app = StringField(max_length=100, required=True)
	sessionTime = IntField(required=True)
	multiSession = BooleanField(required=True)