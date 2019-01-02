#import kivy
#kivy.require("1.10.1")
from kivy.app import App
#kivy.require("1.10.1")

from kivy.uix.label import Label

class SimpleKivy(App):
	def build(self):
		return Label(text = "Hello World")


if __name__ == "__main__":
	SimpleKivy().run()
