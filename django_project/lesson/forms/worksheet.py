# coding=utf-8
"""Section worksheet."""

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Fieldset,
    Field,
    Submit,
)

from lesson.models.worksheet import Worksheet


class WorksheetForm(ModelForm):
    """Form for creating worksheet."""

    class Meta:
        model = Worksheet
        fields = (
            'module',
            'title',
            'summary_leader',
            'summary_text',
            'summary_image',
            'exercise_goal',
            'exercise_task',
            'more_about_text',
            'more_about_image',
        )

    def __init__(self, *args, **kwargs):
        self.section = kwargs.pop('section')
        self.helper = FormHelper()
        layout = Layout(
            Fieldset(
                _('Worksheet details'),
                Field('module', css_class='form_control'),
                Field('title', css_class='form_control'),
                Field('summary_header', css_class='form_control'),
                Field('summary_text', css_class='form_control'),
                Field('summary_image', css_class='form_control'),
                Field('exercise_goal', css_class='form_control'),
                Field('excerise_task', css_class='form_control'),
                Field('more_about_text', css_class='form_control'),
                Field('more_about_image', css_class='form_control'),
                css_id='project-form'
            )
        )

        self.helper.layout = layout
        self.helper.html5_required = False

        super(WorksheetForm, self).__init__(*args, **kwargs)

        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        instance = super(WorksheetForm, self).save(commit=False)
        instance.section = self.section
        instance.save()
        return instance