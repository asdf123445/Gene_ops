import objects_library

#welcome screen or sth

print("Gene-ops CLI version -- testing")




#-----------------main program ----------------------------------------
print(" Type one if you want to acces replication options.\n Type 2 if you want to acces transcription options.\n Type 3 if you want to acces translation options\n")
a = input()
if(a == 1):
    replication_options()
elif( a == 2):
    transription_options()
elif( a == 3):
    translation_options()























#------------------end of main program------------------------------

def replication_options():
    DNA_pattern = objects_library.give_DNA()
    "\n"
    dna = objects_library.Dna()


def transription_options():
    DNA_pattern = objects_library.give_DNA()
    "\n"
    transkryptor = objects_library.Transkryptor()


def translation_options():
    choice = input("Type 1 if you want to translate DNA string, or 2 if RNA string\n")
    if(choice == 1):
        DNA_pattern = objects_library.give_DNA()
        "\n"
        translator = objects_library.Translator()
    elif(choice == 2):
        RNA_pattern = objects_library.give_RNA()
        "\n"
        transkryptor = objects_library.Transkryptor()
        translator = objects_library.Translator()




























# For later uses
#
