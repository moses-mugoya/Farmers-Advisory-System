from django import forms
from .models import Question, SendMail


class DiagnoseForm(forms.Form):
    CHOICE1 = [
        ('sor', 'Sore Throat'),
        ('dre', 'Drenching Sweat'),
        ('ema', 'Emaciation'),
        ('blood', 'Bloody Diarrhoea'),
        ('let', 'Lethargy')
    ]
    CHOICE2 = [
        ('pain', 'Painful Blisters'),
        ('weak', 'Weakness'),
        ('joint', 'Joint Pain'),
        ('Fatigue', 'Fatigue')
    ]
    CHOICE3 = [
        ('Irritability', 'Irritability in infants'),
        ('Loss', 'Weight Loss'),
        ('Anorexia', 'Anorexia'),
        ('abd', 'Abdominal Pain'),
        ('int', 'Exercise Intolerance')
    ]
    CHOICE4 = [
        ('Backache', 'Backache'),
        ('fever', 'Fever'),
        ('moist', 'Moist Cough'),
        ('panting', 'Panting respiration')
    ]
    CHOICE5 = [
        ('red rash', 'Red Rash'),
        ('chills', 'Chills')
    ]

    category1 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICE1,
                                  label='CATEGORY ONE',
                                  required=False)
    category2 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICE2,
                                  label='CATEGORY TWO',
                                  required=False)
    category3 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICE3,
                                  label='CATEGORY THREE',
                                  required=False)
    category4 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICE4,
                                  label='CATEGORY FOUR',
                                  required=False)
    category5 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICE5,
                                  label='CATEGORY FIVE',
                                  required=False)


class PlantsForm(forms.Form):
    CHOICE1 = [
        ('bla', 'Black sooty mould fungus'),
        ('sho', 'ShoesString syndrome'),
        ('for', 'Formation of brown to reddish lesions that enlarge'),
        ('def', 'Defoliation of leaves'),
    ]
    CHOICE2 = [
        ('cri', 'Crinkled leaves'),
        ('wil', 'Wilting and distortion of leaves'),
        ('sun', 'Sunken cankers near the soil line'),
        ('stunt', 'Stunting leaves and stems'),
    ]
    CHOICE3 = [
        ('dry', 'Dry shriveled stem appearance'),
        ('yel', 'Yellowing of leaves'),
        ('lea', 'Leaves mottled with yellow, white and light dark green spots'),
        ('ste', 'Stems decay quickly'),
    ]
    CHOICE4 = [
        ('col', 'Colonies of aphids clustered on leaves'),
        ('stu', 'Stunted growth'),
        ('dyi', 'Wilting and dying of plant'),
        ('mea', 'Mealybugs feed at Stem tips'),
    ]
    CHOICE5 = [
        ('nut', 'Nutrient deficiency stem and leaves'),
        ('hon', 'Honey dews'),
        ('sho', 'Deformed Young growth'),
        ('chl', 'chlorosis'),
    ]

    category1 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICE1,
                                  label='CATEGORY ONE',
                                  required=False)
    category2 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICE2,
                                  label='CATEGORY TWO',
                                  required=False)
    category3 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICE3,
                                  label='CATEGORY THREE',
                                  required=False)
    category4 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICE4,
                                  label='CATEGORY FOUR',
                                  required=False)
    category5 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICE5,
                                  label='CATEGORY FIVE',
                                  required=False)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('subject', 'body')


class MailForm(forms.ModelForm):
    subject = forms.CharField(max_length=250, widget=forms.TextInput)

    class Meta:
        model = SendMail
        fields = ('subject', 'body')
