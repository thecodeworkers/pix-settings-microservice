from mongoengine import EmbeddedDocument, EmbeddedDocumentListField, Document, StringField, BooleanField, DecimalField

class Fee(EmbeddedDocument):
	feeType = StringField(required=True)
	number = DecimalField(required=True)
	calculationType = StringField(required=True)

class Limit(EmbeddedDocument):
	minimum = DecimalField(required=True)
	maximum = DecimalField(required=True)
	limitType = StringField(required=True)


class BusinessSettings(Document):
	app = StringField(max_length=100, required=True)
	fee = EmbeddedDocumentListField(Fee)
	limit = EmbeddedDocumentListField(Limit)
	feeType = StringField(required=True)
	limitType = StringField(required=True)

