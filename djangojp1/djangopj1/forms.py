from django.forms import Form, CharField
 
 
class OyaForm(Form):
    name = CharField(max_length=10)
    addr = CharField(max_length=1024)