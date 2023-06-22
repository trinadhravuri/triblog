from django import forms
from .models import Projects
from django.forms import widgets

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title','description','demo_link','source_link','tag']
    
    def __init__(self,*args,**kwargs):
        super(ProjectsForm,self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['demo_link'].widget.attrs.update({'class':'form-control'})
        self.fields['source_link'].widget.attrs.update({'class':'form-control'})
        self.fields['tag'].widget.attrs.update({'class':'form-control'})


