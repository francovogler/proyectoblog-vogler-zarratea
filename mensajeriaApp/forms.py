from django import forms
from mensajeriaApp.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ('name','content')
        
        widgets={
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
            
        }