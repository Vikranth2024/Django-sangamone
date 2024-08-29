from django import forms

class inputweb(forms.Form):
    input1=forms.IntegerField(min_value=0,max_value=100,label="Enter Number")
