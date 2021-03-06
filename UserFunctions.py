from pymodm import fields, MongoModel, connect


serverConnected = False


def initConnect(
        server='mongodb://test_user:647g04@ds139288.mlab.com:39288//',
        db='systix-sandbox',
        force_connect=False):
    global serverConnected
    if((serverConnected is False) or force_connect):
        connect(
            server.rstrip('/') +
            '/' +
            db)
        serverConnected = True


class User(MongoModel):

    username = fields.CharField()
    password = fields.CharField()


class BankLink(MongoModel):

    user = fields.ReferenceField(User)
    auth_token = fields.CharField()


class BankAccount(MongoModel):

    bank_link = fields.ReferenceField(BankLink)
    number = fields.CharField()
    acc_type = fields.CharField()
