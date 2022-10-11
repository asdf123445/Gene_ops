import objects_library

#welcome screen or sth

print("Gene-ops CLI version -- testing")


def replication_options():
    
    print("replication options")
    #class gets it's object and magic happens
    
    dna = objects_library.Dna()
    objects_library.dna.give_DNA()
    replica = objects_library.dna.do_all_replication()
    print(replica)
    return replica

def transcription_options():
    print("transcription options")
   #class gets it's object and magic happens
    transcriptor = objects_library.Transkryptor()
    objects_library.transcriptor.give_DNA()
    transcript = objects_library.transcriptor.do__all_transcriptor()
    print(transcript)
    return transcript
    del transcriptor

#here there are two options. One for user's own RNA string and one generating RNA string from user's DNA patterns
#both of them work essentially the same as replication_options and translation_options by generating objects from objects_library.py
def translation_options():
    print("translation options","\n")
    choice = input("Type 1 if you want to translate DNA string, or 2 if RNA string\n")
    if(choice == "1"): 
        transcriptor = objects_library.Transkryptor()        
        translator = objects_library.Translator(transcriptor)
        
        translated = objects_library.translator.do_half_translator()
        print(translated)
        return(translated)
        del translator
        del transcriptor    
    elif(choice == "2"):
         
        translator = objects_library.Translator()
        objects_library.translator.give_RNA()
        translated = objects_library.translator.do_all_translator()
        print(translated)
        return(translated)
        del translator
#-----------------main program ----------------------------------------
print(" Type 1 if you want to acces replication options.\n Type 2 if you want to acces transcription options.\n Type 3 if you want to acces translation options\n")
a = input()

if(a == "1"):
    print("something")
    replication_options()
elif( a == "2"):
    transription_options()
elif( a == "3"):
    translation_options()













#------------------end of main program------------------------------





# For later uses
#
