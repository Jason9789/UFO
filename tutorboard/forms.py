from django import forms
from .models import TutorApply, TutorRequest, TutorComment, TuteeComment

class TutorApplyForm(forms.ModelForm):
    class Meta:
        model = TutorApply
        fields = ('title', 'content', 'image')

class TutorRequestForm(forms.ModelForm):
    class Meta:
        model = TutorRequest
        fields = ('title', 'content', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = TutorComment
        fields = ('comment_author', 'comment_contents')


class CommentForm2(forms.ModelForm):
    class Meta:
        model = TuteeComment
        fields = ('comment_author', 'comment_contents')
