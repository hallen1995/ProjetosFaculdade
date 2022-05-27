from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda1"].text = "Bitcoin R$ 350.000"
        self.root.ids["moeda2"].text = "Dólar R$ 5,50"
        self.root.ids["moeda3"].text = "Euro R$ 6,50"
        self.root.ids["moeda4"].text = "Ethereum R$ 250.000"

    # def cotação_da_moeda(self, moeda):
    # link = https://economia.awesomeapi.com.br/last/{moeda}-BRL




MeuAplicativo().run()


