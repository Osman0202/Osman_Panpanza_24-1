from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=100)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField(required=False)
    rate = forms.FloatField(required=False)


class CommentCreateForm(forms.Form):
    title = forms.CharField()