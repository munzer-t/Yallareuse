from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control'}))

    #category = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, 'class':'form-control'}))
    condition = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, 'class':'form-control'}))
    price = forms.FloatField(min_value=1,widget=forms.NumberInput(attrs={'placeholder': 'Price', 'class':'form-control'}, ))


    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'condition', 'price',]


class ProductFileForm(ProductForm):
    file = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(ProductForm.Meta):
        fields = ProductForm.Meta.fields + ['file',]