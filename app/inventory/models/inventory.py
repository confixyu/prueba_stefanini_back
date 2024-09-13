from mongoengine import Document, StringField, DateField


class Inventory(Document):
    name = StringField()
    product_type = StringField()
    serial = StringField()
    date = DateField()
    status = StringField()
