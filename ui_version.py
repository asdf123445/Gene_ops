#This is the ui version of gene ops
#For now it's written in my native language, but soon I'll translate all comments to English

#Also this is really early verion of the file so nothing works and nothing makes any sense :)

import objects_library
import func
import gi 
#gtk module

gi.require_version('Gtk', '3.0')
#wypranie odpowiedniej wersji GTK


from gi.repository import Gtk as gtk
#simplyfying the typing



class Main(func.Functions):
    def __init__ (self):
        gladeFile = "ui.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)
        window = self.builder.get_object("main_window")
        window.connect("delete-event", gtk.main_quit)
        window.show()
        self.replicator = objects_library.Dna()
        self.transcriptor = objects_library.Transcriptor()
        self.translator = objects_library.Translator()

        




    def __del__(self):
        del self.replicator
        del self.transcriptor
        del self.translator
    


    















main = Main()

main.create_all_widgets()
gtk.main()








