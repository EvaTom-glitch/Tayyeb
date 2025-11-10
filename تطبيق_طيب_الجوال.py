# تطبيق_طيب_الجوال.py
from kivy.app import App
from kivy.uix.button import Button

class تطبيقطيب(App):
    def build(self):
        return Button(text='🍕 مرحباً بك في طيب!',
                    size_hint=(0.8, 0.2),
                    pos_hint={'center_x': 0.5, 'center_y': 0.5})

if __name__ == '__main__':
    تطبيقطيب().run() in 
