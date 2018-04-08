from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import json

class Introduction(Page):
    pass

class Survey1(Page):
    form_model = 'player'
    form_fields = [
        'item1A',
        'item1B',
        'item1C',
        'item1D',
        'item1E',
        'item1F',
        'item1G',
        'item1H'
    ]
    form_labels = [
        'item1A',
        'item1B',
        'item1C',
        'item1D',
        'item1E',
        'item1F',
        'item1G',
        'item1H'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class Survey2(Page):
    form_model = 'player'
    form_fields = [
        'item2A',
        'item2B',
        'item2C',
        'item2D',
        'item2E',
        'item2F',
        'item2G',
        'item2H',
        'item2I',
        'item2J'
    ]
    form_labels = [
        'item2A',
        'item2B',
        'item2C',
        'item2D',
        'item2E',
        'item2F',
        'item2G',
        'item2H',
        'item2I',
        'item2J'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'studies', 'workexperience', 'degree', 'english']

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

start_pages = [
    Introduction
]

end_pages = [
    Demographics
]

initial_page_sequence = [
    Survey1,
    Survey2,
]

page_sequence = [

]

class MyPage(Page):
    def inner_dispatch(self):
        page_seq = int(self.__class__.__name__.split('_')[1])
        page_to_show = json.loads(self.participant.vars.get('page_sequence'))[page_seq]
        self.__class__ = globals()[page_to_show]
        return super(globals()[page_to_show], self).inner_dispatch()


for i, _ in enumerate(initial_page_sequence):
    NewClassName = "Survey_{}".format(i)
    A = type(NewClassName, (MyPage,), {})
    locals()[NewClassName] = A
    page_sequence.append(locals()[NewClassName])

page_sequence = start_pages + page_sequence + end_pages
