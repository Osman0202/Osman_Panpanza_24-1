from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField()
    title = forms.CharField(max_length=250)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField(required=False)
    rate = forms.FloatField(required=False)


class CommentCreateForm(forms.Form):
    title = forms.CharField()