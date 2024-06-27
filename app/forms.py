from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class AddProductForm(FlaskForm):
    """Add Product Form"""
    product_name = StringField('product name', validators=[DataRequired(), Length(1, 64)])
    product_description = TextAreaField('product description', validators=[DataRequired()])
    stock_available = SelectField(
        'stock available',
        choices=[
            (1, 1),
            (2, 2),
            (3, 3)
        ],
        validators=[DataRequired()])
    submit = SubmitField('Log In')