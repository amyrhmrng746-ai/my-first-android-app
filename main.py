from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.label = Label(text="سلام! به اپ من خوش آمدی.", font_size='20sp')
        self.text_input = TextInput(hint_text="اینجا چیزی بنویس...", multiline=False, font_size='18sp')
        self.button = Button(text="تایید", size_hint=(1, 0.3), font_size='20sp')
        self.button.bind(on_press=self.on_button_press)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button)
        return self.layout

    def on_button_press(self, instance):
        text = self.text_input.text
        if text:
            self.label.text = f"تو نوشتی: {text}"
            self.text_input.text = ""

if __name__ == '__main__':
    MyApp().run()
