#This program is meant to free my tired mind of performing easy and monotonous genomic operations like 
#replication, transcription or translation.
#This is library of crutial functions and objects 

import string


# to utilize entire classes you shall use do__all methods
# functions give_DNA and give_RNA should be used onli in CLI version of program, until I'll know how to properly 
# implement them in the GUI.

#------------------------------------class beginning--------------------------------------------

# to do: Put give_DNA and give_RNA

class Dna:

#constructor
    def __init__ (self):
        self.DNA_pattern = "" 
        self.reformed = ""
        self.v_replication = ""
        


        
#destructor
    def __del__ (self):
        del self.DNA_pattern
        del self.reformed
        del self.v_replication

    def give_DNA (self):
        self.DNA_pattern = (input("Please input DNA string to analyze    "))
        return self.DNA_pattern


#'just cleaning' function - checks if the DNA string is correct
    def check_string(self):
        for i in range (len(self.DNA_pattern)):
            if( self.DNA_pattern[i] == "a" or self.DNA_pattern[i] == "A"):
                self.reformed += "A"
            elif( self.DNA_pattern[i] == "t" or self.DNA_pattern[i] == "T"):
                self.reformed += "T"
            elif( self.DNA_pattern [i] == "c" or self.DNA_pattern[i] == "C"):
                self.reformed += "C"
            elif( self.DNA_pattern[i] == "g" or self.DNA_pattern[i] == "G"):
                self.reformed += "G"
            else:
                print("Error: wrong sequence")
                break
        return self.reformed


#the name speaks for itself
    def show_sequences (self):
        print(self.reformed)

#the function arranges DNA pattern after replication
    def replication (self):
        for i in range (len(self.reformed)):
            if( self.DNA_pattern[i] == "A"):
                self.v_replication  += "T"
            elif( self.DNA_pattern[i] == "T"):
                self.v_replication += "A"
            elif( self.DNA_pattern [i] == "C"):
                self.v_replication += "G"
            elif( self.DNA_pattern[i] == "G"):
                self.v_replication += "C"
        return self.v_replication



#One method to rule them all

    def do_all_replication(self):
        self.check_string()
        self.a = input("type 1 to show DNA string   ")
        if(self.a == "1"):
            self.show_sequences()
        self.replication()
        return self.v_replication





#---------------------------------------class end--------------------------------------------





#---------------------------------------class beginning----------------------------------------


class Transcriptor:

#constructor
    def __init__ (self):
        self.DNA_pattern = ""
        self.reformed = ""
        self.z_transcription = ""


#destructor
    def __del__ (self):
        del self.DNA_pattern
        del self.reformed
        del self.z_transcription


    def give_DNA (self):
            self.DNA_pattern = (input("Please input DNA string to analyze"))
            return self.DNA_pattern


#'just cleaning' function - checks if the DNA string is correct
    def check_stringr(self):
        for i in range (len(self.DNA_pattern)):
            if( self.DNA_pattern[i] == "a" or self.DNA_pattern[i] == "A"):
                self.reformed += "A"
            elif( self.DNA_pattern[i] == "t" or self.DNA_pattern[i] == "T"):
                self.reformed += "T"
            elif( self.DNA_pattern [i] == "c" or self.DNA_pattern[i] == "C"):
                self.reformed += "C"
            elif( self.DNA_pattern[i] == "g" or self.DNA_pattern[i] == "G"):
                self.reformed += "G"
            else:
                print("Error: incorrect sequence")
                break
        return self.reformed

#the name speaks for itself
    def show_sequences (self):
        print(self.reformed)

#transcripting function, DNA to RNA
    def transcription (self):
        for i in range (len(self.reformed)):
            if( self.DNA_pattern[i] == "A"):
                self.z_transcription += "U"
            elif( self.DNA_pattern[i] == "T"):
                self.z_transcription += "A"
            elif( self.DNA_pattern [i] == "C"):
                self.z_transcription += "G"
            elif( self.DNA_pattern[i] == "G"):
                self.z_transcription += "C"
        return self.z_transcription



#One method to rule them all
    def do_all_transcriptor(self):
        self.check_stringr()
        self.a = input("type 1 to show DNA string   ")
        if(self.a == "1"):
            self.show_sequences()
        self.transcription()
        return self.z_transcription

    def do_all_transcriptor_tb(self):
        self.DNA_pattern = give_DNA
        self.reformed = sprawdz_string()
        self.a = input("type 1 to show DNA string   ")
        if(self.a == "1"):
            self.show_sequences()
        self.transcription()
        return self.z_transcription


#--------------------------------------------class end--------------------------------







#-------------------------------------------class beginning-----------------------------

#class storing translation operations, from RNA to protein
class Translator:

#constructor
    def __init__ (self):
        self.RNA_pattern = ""
        self.reformed = ""
        self.codons = ""
        self.protein = ""
        self.DNA_pattern = ""
        self.z_transcription = ""
#destructor
    def __del__ (self):
        del self.RNA_pattern
        del self.reformed
        del self.codons
        del self.protein
        del self.DNA_pattern
        del self.z_transcription
#translation from RNA
    def give_RNA (self):
        self.RNA_pattern = (input("Please input RNA string to analyze  "))
        return self.RNA_pattern
#translation from DNA

    def give_DNA (self):
            self.DNA_pattern = (input("Please input DNA string to analyze"))
            return self.DNA_pattern

# transcripting function
    def transcription (self):
        for i in range (len(self.DNA_pattern)):
            if( self.DNA_pattern[i] == "A"):
                self.z_transcription += "U"
            elif( self.DNA_pattern[i] == "T"):
                self.z_transcription += "A"
            elif( self.DNA_pattern [i] == "C"):
                self.z_transcription += "G"
            elif( self.DNA_pattern[i] == "G"):
                self.z_transcription += "C"
        return self.z_transcription

#checking function
    def check_stringr(self):
        for i in range (len(self.z_transcription)):
            if( self.z_transcription[i] == "a" or self.z_transcription[i] == "A"):
                    self.reformed += "A"
            elif( self.z_transcription[i] == "u" or self.z_transcription[i] == "U"):
                    self.reformed += "U"
            elif( self.z_transcription [i] == "c" or self.z_transcription[i] == "C"):
                    self.reformed += "C"
            elif( self.z_transcription[i] == "g" or self.z_transcription[i] == "G"):
                    self.reformed += "G"
            else:
                    print("Error: incorrect sequence")
                    break
        print("reformed", self.reformed) 
        return self.reformed
        


#Horror begins
    def find_codons (self):
        for i in range (len(self.reformed)):
            for j in range (len(self.reformed)/3):
                self.kodon[j] = self.reformed[i] + self.reformed[i + 1] + self.reformed[i + 2]
                
            i += 3
        return self.codons

#translation from codons
    def translator (self):

# self.protein is a list storing individual aminoacids a.k.a  storing protein's pattern'
# I thought that it will be more efficient to declare the lenght before, instead of using .append over and over
        self.protein [(len(self.codons))]


        for i in range (len(self.codons)):
            if(self.codons[i] == AUG):
                self.protein += "  Met  ,"
            elif(self.codons[i] == "UUU" or self.codons[i] == "UUC"):
                self.protein += "  Phe  ,"
            elif(self.codons[i] == "UUA" or self.codons[i] == "UUG" or self.codons[i] == "CUU" or self.codons[i] == "CUC" or self.codons[i] == "CUA" or self.codons[i] == "CUG"):
                self.protein += "  Leu  ,"
            elif(self.codons[i] == "AUU" or self.codons[i] == "AUC" or self.codons[i] == "AUA"):
                self.protein += "  Ile  ,"
            elif(self.codons[i] == "GUU" or self.codons[i] == "GUC" or self.codons[i] == "GUA" or self.codons[i] == "GUG"):
                self.protein += "  Val  ,"
            elif(self.codons[i] == "UCU" or self.codons[i] == "UCC" or self.codons[i] == "UCA" or self.codons[i] == "UCG"):
                self.protein += "  Ser  ,"
            elif(self.codons[i] == "CCU" or self.codons[i] == "CCC" or self.codons[i] == "CCA" or self.codons[i] == "CCG"):
                self.protein += "  Pro  ,"
            elif(self.codons[i] == "ACU" or self.codons[i] == "ACC" or self.codons[i] == "ACA" or self.codons[i] == "ACG"):
                self.protein += "  Thr  ,"
            elif(self.codons[i] == "GCU" or self.codons[i] == "GCC" or self.codons[i] == "GCA" or self.codons[i] == "GCG"):
                self.protein += "  Ala  ,"
            elif(self.codons[i] == "UAU" or self.codons[i] == "UAC"):
                self.protein += "  Tyr  ,"
            elif(self.codons[i] == "UAA" or self.codons[i] == "UAG"):
                self.protein += "  STOP  ,"
            elif(self.codons[i] == "CAU" or self.codons[i] == "CAC"):
                self.protein += "  His  ,"
            elif(self.codons[i] == "CAA" or self.codons[i] == "CAG"):
                self.protein += "  Gln  ,"
            elif(self.codons[i] == "AAU" or self.codons[i] == "AAC"):
                self.protein += "  Asn  ,"
            elif(self.codons[i] == "AAA" or self.codons[i] == "AAG"):
                self.protein += "  Lys  ,"
            elif(self.codons[i] == "GAU" or self.codons[i] == "GAC"):
                self.protein += "  Asp  ,"
            elif(self.codons[i] == "GAA" or self.codons[i] == "GAG"):
                self.protein += "  Glu  ,"
            elif(self.codons[i] == "UGU" or self.codons[i] == "UGC"):
                self.protein += "  Cys  ,"
            elif(self.codons[i] == "UGG"):
                self.protein += "  Trp  ,"
            elif(self.codons[i] == "CGU" or self.codons[i] == "CGC" or self.codons[i] == "CGA" or self.codons[i] == "CGG"):
                self.protein += "  Arg  ,"
            elif(self.codons[i] == "GGU" or self.codons[i] == "GGC" or self.codons[i] == "GGA" or self.codons[i] == "GGG"):
                self.protein += "  Gly  ,"
            else:
                self.protein += "  RRR  ,"

        return self.protein


#One method to rule them all
    def do_all_translator(self):
        self.check_string()
        self.find_codons()
        self.translator ()
        return self.protein
    

    def do_half_translator(self):
        self.transcription()
        print("do half")
        self.check_stringr()
        print(self.reformed)
        self.find_codons()
        self.translator()
        return self.protein
        



#-----------------------------------------------class end-------------------------------------
