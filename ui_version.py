#This is the ui version of gene ops
#For now it's written in my native language, but soon I'll translate all comments to English

#Also this is really early verion of the file so nothing works and nothing makes any sense :)

import objects_library
import gi 
#gtk module

gi.require_version('Gtk', '3.0')
#wypranie odpowiedniej wersji GTK


from gi.repository import Gtk as gtk
#simplyfying the typing



class Main:
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
    #to keep the code clean i wrote second constructor for buttons etc
    def __init__(self):




    def __del__(self):
        del self.replicator
        del self.transcriptor
        del self.translator

    

   
        
















#function for initiating all buttons etc. to keep the consctructor clean
    def create_widgets (self):
        #refresh button
        refresh_button = self.builder.get_objects("panel_button_refresh")
        refresh_button.connect("clicked", self.refresh_all)
 


   #function for refresh button 
    def refresh_all (self):
        self.replicator.refresh()
        self.transcriptor.refresh()
        self.translator.refresh()

#function for replication input field in glade
    def insert_repl (self):
        repl = self.builder.get_object("replication_entry")
        self.repltask = repl.get_text().strip()
        return self.repltask
#function for transcription input field in glade   
    def insert_transc(self):
        transc = self.builder.get_object("replication_entry")
        self.transctask = transc.get_text().strip()
        return self.transctask
#function for translation input field in glade
    def insert_transl(self):
        transl = self.builder.get_object("translation_entry")
        self.transltask = transl.get_text().strip()
        return self.transltask




main = Main()
gtk.main()







