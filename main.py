from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.core.window import Window

Window.size = (360, 600)

class CalculadoraApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        
        layout_principal = MDBoxLayout(orientation='vertical', padding=15, spacing=10)
        
        label_titulo = MDLabel(
            text="📱 Calculadora Veterinaria",
            font_style="H6",
            halign="center",
            size_hint_y=0.1,
            theme_text_color="Hint"
        )
        layout_principal.add_widget(label_titulo)
        
        self.pantalla = MDLabel(
            text="",
            font_style="H3",
            halign="right",
            valign="bottom",
            size_hint_y=0.25,
            theme_text_color="Primary",
            padding=(10, 10)
        )
        self.pantalla.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        layout_principal.add_widget(self.pantalla)
        
        grid_botones = MDGridLayout(cols=4, spacing=12, size_hint_y=0.65)
        
        botones = [
            'C', '(', ')', '÷',
            '7', '8', '9', '×',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '⌫', '='
        ]
        
        for texto in botones:
            if texto in ['÷', '×', '-', '+', '=']:
                color_btn = (0.6, 0.2, 0.8, 1)
            elif texto == 'C':
                color_btn = (0.9, 0.2, 0.2, 1)
            elif texto == '⌫':
                color_btn = (0.7, 0.4, 0.1, 1)
            else:
                color_btn = (0.25, 0.25, 0.25, 1)
                
            btn = MDRaisedButton(
                text=texto,
                font_size="24sp",
                size_hint=(1, 1),
                md_bg_color=color_btn,
                text_color=(1, 1, 1, 1),
                on_release=self.on_boton_presionado
            )
            grid_botones.add_widget(btn)
            
        layout_principal.add_widget(grid_botones)
        return layout_principal

    def on_boton_presionado(self, instancia):
        texto_boton = instancia.text
        texto_actual = self.pantalla.text
        
        if texto_boton == '×':
            texto_boton = '*'
        elif texto_boton == '÷':
            texto_boton = '/'
        
        if texto_boton == 'C':
            self.pantalla.text = ""
        elif texto_boton == '⌫':
            if "Error" in texto_actual:
                self.pantalla.text = ""
            else:
                self.pantalla.text = texto_actual[:-1]
        elif texto_boton == '=':
            try:
                resultado = str(eval(texto_actual))
                self.pantalla.text = resultado
            except ZeroDivisionError:
                self.pantalla.text = "Error: Div / 0"
            except Exception:
                self.pantalla.text = "Error"
        else:
            if "Error" in texto_actual:
                self.pantalla.text = texto_boton
            else:
                self.pantalla.text += texto_boton

if __name__ == '__main__':
    CalculadoraApp().run()
