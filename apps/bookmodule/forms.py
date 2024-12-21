from django import forms
from .models import Book,Student,Address,Student2,ImageTable

class BookForm(forms.ModelForm):
    class Meta: 
        model = Book 
        fields = ['title', 'author', 'price', 'edition']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields='__all__'
        exclude = []
    name = forms.CharField(max_length=100,label='Name',required=True,widget=forms.TextInput())
    age = forms.IntegerField(initial=0,label='Age',required=True,widget=forms.NumberInput())
    address=forms.ModelChoiceField(label='City',queryset=Address.objects.all(),required=True, widget=forms.Select())

class StudentForm2(forms.ModelForm):
    class Meta:
        model= Student2
        fields='__all__'
        exclude = []
    name = forms.CharField(max_length=100,label='Name',required=True,widget=forms.TextInput())
    age = forms.IntegerField(initial=0,label='Age',required=True,widget=forms.NumberInput())
    addresses=forms.ModelMultipleChoiceField(label='City',queryset=Address.objects.all(),required=True, widget=forms.CheckboxSelectMultiple())

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageTable
        fields = ['title', 'image']