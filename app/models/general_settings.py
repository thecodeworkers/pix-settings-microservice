from mongoengine import Document, StringField, IntField, BooleanField

class GeneralSettings(Document):
	app = StringField(min_length=2,max_length=100, required=True)
	sessionTime = IntField(min_value=1,required=True)
	multiSession = BooleanField(required=True)