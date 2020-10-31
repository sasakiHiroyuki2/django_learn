from django.forms import ModelForm
from . models import Topic, Category, Comment
from django import forms


class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title',
            'user_name',
            'category',
            'message',
        ]


class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title',
            'user_name',
            'category',
            'message',
        ]

    def __init__(self, *args, **kwargs):
        # kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '選択して下さい'
        self.fields['user_name'].widget.attrs['value'] = '匿名'
        # self.fields['title'].widget.attrs['class'] = 'huga'


class TopicForm(forms.Form):
    title = forms.CharField(
        label='タイトル',
        max_length=255,
        required=True,
    )
    user_name = forms.CharField(
        label='お名前',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'value': '名無し'}),
    )
    category = forms.ModelChoiceField(
        label='カテゴリー',
        queryset=Category.objects.all(),
        required=True,
        empty_label='選択して下さい',
    )
    message = forms.CharField(
        label='本文',
        widget=forms.Textarea,
        required=True,
    )


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'user_name',
            'message',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs['value'] = '名無し'

    def save_with_topic(self, topic_id, commit=True):
        comment = self.save(commit=False)
        comment.topic = Topic.objects.get(id=topic_id)
        comment.no = Comment.objects.filter(topic_id=topic_id).count() + 1
        if commit:
            comment.save()
        return comment
