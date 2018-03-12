from wtforms import Form, BooleanField, StringField, validators, DateTimeField, TextAreaField, IntegerField

print ("Hello, Python!")

class RegistrationForm(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])

class ProfileForm(Form):
    birthday  = DateTimeField('Your Birthday', format='%m/%d/%y')
    signature = TextAreaField('Forum Signature')

class AdminProfileForm(ProfileForm):
    username = StringField('Username', [validators.Length(max=40)])
    level    = IntegerField('User Level', [validators.NumberRange(min=0, max=10)])

def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST' and form.validate():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.save()
        redirect('register')
    return render_response('register.html', form=form)

from wtforms import Form, StringField, validators
class UsernameForm(Form):
    username = StringField('Username', [validators.Length(min=5)], default=u'test')

class LoginForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')

form = LoginForm()

#form = UsernameForm()
#x = form['username']
#form2 = UsernameForm(username=u'Robert')
#n = 1
