from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
FloatLayout:
    MDRaisedButton:
        text: 'Clique Aqui'
'''

class Tela(MDApp):
    def tela_principal(self):
        return Builder.load_string(KV)