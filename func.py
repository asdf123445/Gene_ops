import objects_library




class Functions:
#function for initiating all buttons etc. to keep the consctructor clean

    def __init__ (self):
        print("functions ready!")

    def __del__ (self):
        del self.repltask
        del self.transctask
        del self.transltask
        del self.refresh_button
        del self.show_button_repl
        del self.show_button_transc
        del self.show_button_transl
        del self.replication_entry
        del self.transcription_entry
        del self.translation_entry
        del self.replication_go
        del self.transcription_go
        del self.translation_go
        del self.repl_text
        del self.transc_text
        del self.transl_text


    def create_widgets (self):
        #refresh button
        refresh_button = self.builder.get_objects("panel_button_refresh")
        refresh_button.connect("clicked", self.refresh_all)

    def create_widgets2 (self):
        #block of code using show string buttons
        show_button_repl = self.builder.get_objects("replication_button_check")
        show_button_transc = self.builder.get_objects("transcription_button_check")
        show_button_transl = self.builder.get_objects("translation_button_check")
        show_button_repl.connect("toggled", self.show_string_rp)
        show_button_transc.connect("toggled", self.show_string_tc)
        show_button_transc.connect("toggled", self.show_string_tl)

    def create_widgets3 (self):
        #creator and connector of entry fields
        replication_entry = self.builder.get_objects("replication_entry")
        transcription_entry = self.builder.get_objects("transcription_entry")
        translation_entry = self.builder.get_objects("translation_entry")
        replication_entry.connect("changed", self.insert_repl)
        transcription_entry.connect("changed", self.insert_transc)
        translation_entry.connect("changed", self.insert_transl)

    def create_widgets4 (self):
        #creator and connector of go buttons
        raplication_go = self.builder.get_objects("replication_button_go")
        replication_go.connect("clicked", self.go_repl)
        transcription_go = self.builder.get_objects("transcription_button_go")
        transcription_go.connect("clicked", self.go_transc)
        translation_go = self.builder.get_objects("translation_button_go")
        translation_go = connect("clicked", self.go_transl)

    def create_widgets5 (self):
        #creator and connector of results text fields
        self.repl_text = self.builder.get_objects("replication_text_results")
        self.transc_text = self.builder.get_objects("transcription_text_results")
        self.transl_text = self.builder.get_objects("translation_text_results")
        
    def create_widgets6 (self):
        repl_opt1 = self.builder.get_objects("translation_button_left")
        repl_opt2 = self.builder.get_objects("translation_button_right")
        repl_opt1.connect("clicked", self.replop1)
        repl_opt2.connect("clicked", self.replop2)

    def create_all_widgets (self):
        #creator of all (for quickly creating everything)
        self.create_widgets()
        self.create_widgets2()
        self.create_widgets3()
        self.create_widgets4()
        self.create_widgets5()
        self.create_widgets6()

#functions for setting show string parameter (self.a)
    def show_string_rp (self, replicator):
        self.replicator.a = "0"

    def show_string_tc (self, transcriptor):
        self.transcriptor.a = "0"

    def show_string_tl (self, translator):
        self.translator.a = "0"

    def replop1 (self, translator):
        self.translator.b = "0"
    def replop2 (self, translator):
        self.translator.b = "1"

#function for refresh button
    def refresh_all (self, objects_library):
        self.replicator.refresh()
        self.transcriptor.refresh()
        self.translator.refresh()


#function for replication input field in glade
    def insert_repl (self):
        self.replicator.DNA_pattern = self.replication_entry.get_text().strip()


#function for transcription input field in glade
    def insert_transc(self):
        self.transcriptor.DNA_pattern = self.transcription_entry.get_text().strip()


#function for translation input field in glade
    def insert_transl(self):
        self.translator.DNA_pattern = self.translation_entry.get_text().strip()



#functions for go button
    def go_repl (self, replicator, repl_text):
        repl_text.TextBuffer.set_text(self.replicator.do_all_replication_v())
    
    def go_transc(self,transcriptor, transc_text):
        transc_text.TextBuffer.set_text(self.transcriptor.do_all_transcriptor_v())        
    def go_transl(self, translator, transl_text):
        if(self.translator.b == "0"):
            transc_text.TextBuffer.set_text(self.translator.do_half_translator_v())
        elif(self.translator.b =="1"):
            transl_text.TextBuffer.set.text(self.translator.do_all_translator_v())





