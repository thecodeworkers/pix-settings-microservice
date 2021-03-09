from mongoengine import EmbeddedDocument, EmbeddedDocumentListField, Document, StringField, BooleanField, DecimalField

class Fee(EmbeddedDocument):
	feeType = StringField(min_length=2,required=True)
	number = DecimalField(required=True)
	calculationType = StringField(min_length=2,required=True)

class Limit(EmbeddedDocument):
	minimum = DecimalField(required=True)
	maximum = DecimalField(required=True)
	limitType = StringField(min_length=2,required=True)


class BusinessSettings(Document):
	app = StringField(min_length=2,max_length=100, required=True, unique=True)
	fee = EmbeddedDocumentListField(Fee)
	limit = EmbeddedDocumentListField(Limit)
	feeType = StringField(min_length=2,required=True)
	limitType = StringField(min_length=2,required=True)

