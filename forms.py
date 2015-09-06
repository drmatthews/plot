from django import forms
from django.forms import ChoiceField,MultipleChoiceField,IntegerField,CharField

class PreviewForm(forms.Form):
    def __init__(self, options=None, *args, **kwargs):
        super(PreviewForm, self).__init__(*args, **kwargs)
        self.fields['preview_annotation'].choices = options

    preview_annotation = ChoiceField(choices=(),required=True)
    preview_sheet = IntegerField(required=False,min_value=0)
    
class AnnotationsForm(forms.Form):
    def __init__(self, options=None, *args, **kwargs):
        super(AnnotationsForm, self).__init__(*args, **kwargs)
        self.fields['annotation'].choices = options

    annotation = ChoiceField(choices=(),required=True)
    header = IntegerField(required=False,min_value=0)
    sheet = IntegerField(required=False,min_value=0)
    
class GraphForm(forms.Form):
    def __init__(self, options=None, *args, **kwargs):
        super(GraphForm, self).__init__(*args, **kwargs)
        self.fields['x_data'].choices = options
        self.fields['y_data'].choices = options

    title = CharField(max_length=200,required=False)
    x_Label = CharField(max_length=50,required=False)
    y_Label = CharField(max_length=50,required=False)
    #tick_size = IntegerField(required=False,min_value=1)
    plot_type = ChoiceField(choices=(('',''),('bar','bar'),
                                            ('line','line'),\
                                            ('scatter','scatter'),\
                                            ('scatter+line','scatter+line')),\
                                            required=True)
    x_data = ChoiceField(choices=(),required=True)
    y_data = MultipleChoiceField(choices=(),required=True)