from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(Screen):
    pass

class PasswordScreen(Screen):
    pass

class TwitterPassword(Screen):
    pass

class TiktokPassword(Screen):
    pass

class FacebookPassword(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class PasswordManager(App):
    def build(self):
        return kv

if __name__ == '__main__':
    PasswordManager().run()