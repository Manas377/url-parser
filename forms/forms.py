from django import forms


class Form(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'Enter URL Here...'}), label='')

    def clean(self):
        cleaned_data = super(Form, self).clean()
        url = cleaned_data.get('url')
        if not url:
            raise forms.ValidationError('url is wrong')