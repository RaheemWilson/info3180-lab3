from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', 
                        validators=[DataRequired()], 
                        description="Please enter your full name"
                    )
    email = StringField('Email', 
                        validators=[DataRequired()],
                        description="Please enter your e-mail address"
                    )
    subject = StringField('Subject', 
                            validators=[DataRequired()],
                            description="Please enter the subject for your message"
                        )
    message = TextAreaField('Message',
                            validators=[DataRequired()],
                            description="Please enter the message you would like to send"
                        )