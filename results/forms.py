from django import forms
from .models import Result

# class ResultEntryForm(forms.Form):
#     polling_unit_number = forms.CharField(max_length=50, required=True)
#     party_results = forms.ModelMultipleChoiceField(
#         queryset=Party.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True,
#     )

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['party', 'polling_unit_number', 'votes'] 

    def __init__(self, *args, **kwargs):
        super(ResultForm, self).__init__(*args, **kwargs)
        
