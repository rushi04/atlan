from django import forms

#inheritance form forms.Form class
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()