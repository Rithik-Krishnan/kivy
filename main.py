from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.clock import Clock
import hashlib
import hmac
import time
import pyotp


class MyLabel(Label):
    def __init__(self, key, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.text = "Generating OTP... "
        Clock.schedule_interval(self.update_otp, 10)

    def update_otp(self, dt):
        otp = self.generate_totp(self.key)
        self.text = f"OTP : {otp}"

    def generate_totp(self, key):
        totp = pyotp.TOTP(key)
        rnow = totp.now()
    
        return str(rnow).zfill(6)


class MyApp(App):
    def build(self):
        self.title = 'Authenticator'
        key = "5BRYRIS55DNQNJPBGTTTOHZQRJDXYFGB"
        return MyLabel(key=key)


if __name__ == '__main__':
    MyApp().run()
