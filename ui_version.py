#This is the ui version of gene ops
#For now it's written in my native language, but soon I'll translate all comments to English

import objects_library
import gi 
#moduł gtk

gi.require_version('Gtk', '3.0')
#wypranie odpowiedniej wersji GTK


gi.repository import Gtk = gtk
#nie wiem co to robi ale ok




class Main
    def __init__ (self):
        gladeFile = "main.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file_(gladeFile)


        button = self.builder.get_object("button")
        button.connect()




if __name__ == "__main__":
    main = Main()
    gtk.main()

