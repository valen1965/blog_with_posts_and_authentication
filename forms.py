from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users

class RegisterForm(FlaskForm):
    name = StringField(label="Name", render_kw={"placeholder": "Username"}, validators=[DataRequired()])
    email = StringField(label="Email", render_kw={"placeholder": "Email"}, validators=[DataRequired()])
    password = PasswordField(label="Password", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    submit = SubmitField(label="Sign Me Up!")


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField(label="Email", render_kw={"placeholder": "Email"}, validators=[DataRequired()])
    password = PasswordField(label="Password", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


# TODO: Create a CommentForm so users can leave comments below posts

class CommentForm(FlaskForm):
    comment = CKEditorField(label="Comment", validators=[DataRequired()])
    submit = SubmitField(label="Submit Comment")