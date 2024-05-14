from kivymd.app import MDApp
from kivy.lang import Builder

from banco import criar_banco_de_dados

KV = '''
FloatLayout:
    MDRaisedButton:
        text: 'Clique Aqui'
        #on_press: app.criar_bd()
'''

class Tela(MDApp):
    def build(self):
        criar_banco_de_dados()
        return Builder.load_string(KV)
    
    #def criar_bd(self):
        #criar_banco_de_dados() 