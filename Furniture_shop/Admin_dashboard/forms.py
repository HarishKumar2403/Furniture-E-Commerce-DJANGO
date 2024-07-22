from django import forms
from .models import *


    
class Bedform(forms.ModelForm):
   def __init__(self, *args, **kwargs):
        super(Bedform, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
   

   class Meta:
      model=Product
      exclude=['user_id','status','new','trending','out_of_stock','Category_name']

