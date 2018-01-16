from flask_restful import Resource, request

from wtforms import Form, StringField, PasswordField, validators

from util.form import check


class NewUserForm(Form):
    phone = StringField('User Phone number', [validators.DataRequired()])
    password = PasswordField('User password', [validators.DataRequired()])


class NewUser(Resource):
    @check(NewUserForm)
    def post(self):
        form = NewUserForm(request.form)
        return 'create.py'
