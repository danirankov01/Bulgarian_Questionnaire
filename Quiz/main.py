# It creates the application’s life cycle
from kivy.app import App

# Widget which manages multiple screens and performs animations
from kivy.uix.screenmanager import Screen, ScreenManager

# The builder it's creating parser which parse the .kv file
from kivy.lang import Builder

# Instance object with whom we avoid problem where the config file settings are not applied before window creation
from kivy.config import Config

# From the imported config object we got built-in method with whom we set the size of the app
Config.set('graphics', 'Resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')


# First page of the app when you start it
class HomePage(Screen):
    pass


# In the .py file we only define the classes of every page in the app
# All of the further classes are empty because the business logic is contained in the .kv file

# Also every class inherit Screen class. This way we make our app with
# dynamic pages and we can attach previous and next button so we can go through the pages
class Question1(Screen):
    pass


class Question2(Screen):
    pass


class Question3(Screen):
    pass


class Question4(Screen):
    pass


class Question5(Screen):
    pass


class Question6(Screen):
    pass


class Question7(Screen):
    pass


class Question8(Screen):
    pass


class Question9(Screen):
    pass


class Question10(Screen):
    pass


class FinalPage(Screen):
    pass


# The final class inherit ScreenManager class, as I said upward it's responsible to manage multiple screen is the app
class ScreenManagement(ScreenManager):
    pass


# built-in function which load the kivy file
file = Builder.load_file('file.kv')


# The main class which return the .kv file
class QuizApp(App):
    def build(self):
        return file


QuizApp().run(
