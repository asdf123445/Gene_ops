#celem tego programu jest odciążenie mojego biednego umysłu od trudów obliczania
#replikacji transkrypcji i translacji. Jest to moja biblioteka xd :).

import string


def give_DNA ():
    DNA_pattern = (input("Please input DNA string to analyze"))
    return DNA_pattern

def give_RNA ():
    RNA_pattern = (input("Please input RNA string to analyze"))
    return RNA_pattern

#------------------------------------class beginning--------------------------------------------
class Dna :

#constructor
    def __init__ (self, DNA_pattern):
        self.string_DNA = DNA_pattern

#destructor
    def __del__ (self):
        del self.string_DNA
        del self.lenght
        del self.reformed
        del self.v_replication


#'just cleaning' function - checks if the DNA string is correct
    def check_string(self, string_DNA):
        self.lenght = len(self.string_DNA)
        string(self.reformed)
        for i in range (lenght):
            if( self.string_DNA[i] == a or A):
                self.reformed[i] = A
            elif( self.string_DNA[i] == t or T):
                self.reformed[i] = T
            elif( self.string_DNA [i] == c or C):
                self.reformed[i] = C
            elif( self.string_DNA[i] == g or G):
                self.reformed[i] = G
            else:
                print("Error: wrong sequence")
                break
        return self.reformed


#the name speaks for itself
    def show_sequences (self, reformed):
        print(self.reformed)

#the function arranges DNA pattern after replication
    def replication (self, reformed):
        string(self.v_replication)
        for i in range (len(self.reformed)):
            if( self.string_DNA[i] == A):
                self.v_replication[i] = T
            elif( self.string_DNA[i] == T):
                self.v_replication[i] = A
            elif( self.string_DNA [i] == C):
                self.v_replication[i] = G
            elif( self.string_DNA[i] == G):
                self.v_replication[i] = C
        return self.v_replication

    def show_anti_sense_squences(self, v_replication):
        print(self.replication)


#One method to rule them all

    def do_all_replication():
        self.reformed = check_string(self, string_DNA)
        self.a = insert("type 1 to show DNA string")
        if(self.a == 1):
            show_sequences(self, reformed)
        self.v_replication = replication(self, reformed)
        self.b = insert("type 1 to show anti - sence DNA string")
        if(self.b == 1):
            show_anti_sense_squences(self, reformed)
        return self.v_replication





#---------------------------------------class end--------------------------------------------





#---------------------------------------class beginning----------------------------------------


class Transkryptor:

#constructor
    def __init__ (self):
        self.string_DNA = DNA_pattern
#destructor
    def __del__ (self):
        del self.string_DNA
        del self.reformed
        del self.lenght
        del self.z_transcription
        del self.z_transcription_w



#'just cleaning' function - checks if the DNA string is correct
    def sprawdz_string(self, string_DNA):
        self.lenght = len(self.string_DNA)
        string(self.reformed)
        for i in range (lenght):
            if( self.string_DNA[i] == a or A):
                self.reformed[i] = A
            elif( self.string_DNA[i] == t or T):
                self.reformed[i] = T
            elif( self.string_DNA [i] == c or C):
                self.reformed[i] = C
            elif( self.string_DNA[i] == g or G):
                self.reformed[i] = G
            else:
                print("Error: incorrect sequence")
                break
        return self.reformed

#the name speaks for itself
    def show_sequences (self, reformed):
        print(self.reformed)

#transcripting function, DNA to RNA
    def transcription (self, reformed):
        string(self.z_transcription)
        for i in range (len(self.reformed)):
            if( self.string_DNA[i] == A):
                self.z_transcription[i] = U
            elif( self.string_DNA[i] == T):
                self.z_transcription[i] = A
            elif( self.string_DNA [i] == C):
                self.z_transcription[i] = G
            elif( self.string_DNA[i] == G):
                self.z_transcription[i] = C
        return self.z_transcription


#reverse transcripting function, RNA to DNA
    def transcription_reverse (self, reformed):
        string(self.z_transcription_w)
        for i in range (len(self.reformed)):
            if( self.string_DNA[i] == A):
                self.z_transcription_w[i] = T
            elif( self.string_DNA[i] == U):
                self.z_transcription_w[i] = A
            elif( self.string_DNA [i] == C):
                self.z_transcription_w[i] = G
            elif( self.string_DNA[i] == G):
                self.z_transcription_w[i] = C
        return self.z_transcription_w

#One method to rule them all
    def do_all_transcriptor():
        self.reformed = sprawdz_string(self, string_DNA)
        self.a = insert("type 1 to show DNA string")
        if(self.a == 1):
            show_sequences(self, reformed)
        self.z_transcription = transcription(self, reformed)
        self.b = insert("type 1 to perform reverse transcription")
        if(self.b == 1):
            transcription_reverse(self, reformed)
            return self.z_transcription_w
        return self.z_transcription


#--------------------------------------------class end--------------------------------







#-------------------------------------------class beginning-----------------------------

#class storing translation operations, from RNA to protein
class Translator:

#constructor
    def __init__ (self, RNA_pattern):
        self.string_RNA = RNA_pattern

#destructor
    def __del__ (self):
        del self.string_RNA
        del self.reformed
        del self.codons
        del self.protein

#Again the string needs to be checked
    def check_string(self, string_RNA):
            self.lenght = len(self.string_RNA)
            string(self.reformed)
            for i in range (lenght):
                if( self.string_RNA[i] == a or A):
                    self.reformed[i] = A
                elif( self.string_RNA[i] == u or U):
                    self.reformed[i] = U
                elif( self.string_RNA [i] == c or C):
                    self.reformed[i] = C
                elif( self.string_RNA[i] == g or G):
                    self.reformed[i] = G
                else:
                    print("Error: wrong sequence")
                    break
            return self.reformed

#Horror begins
    def find_codons (self, reformed):
        for i in range (len(self.reformed)):
            for j in range (len(self.reformed/3)):
                self.kodon[j] = self.reformed[i] + self.reformed[i + 1] + self.reformed[i + 2]
                i = i + 3
        return self.codons

#translation from codons
    def translator (self, codons):

# self.protein is a list storing individual aminoacids a.k.a  storing protein's pattern'
# I thought that it will be more efficient to declare the lenght before, instead of using .append over and over
        self.protein [(len(self.codons))]


        for i in range (len(self.codons)):
            if(self.codons[i] == AUG):
                self.protein[i] = "  Met  ,"
            elif(self.codons[i] == UUU or UUC):
                self.protein[i] == "  Phe  ,"
            elif(self.codons[i] == UUA or UUG or CUU or CUC or CUA or CUG):
                self.protein[i] = "  Leu  ,"
            elif(self.codons[i] == AUU or AUC or AUA):
                self.protein[i] = "  Ile  ,"
            elif(self.codons[i] == GUU or GUC or GUA or GUG):
                self.protein[i] = "  Val  ,"
            elif(self.codons[i] == UCU or UCC or UCA or UCG):
                self.protein[i] = "  Ser  ,"
            elif(self.codons[i] == CCU or CCC or CCA or CCG):
                self.protein[i] = "  Pro  ,"
            elif(self.codons[i] == ACU or ACC or ACA or ACG):
                self.protein[i] = "  Thr  ,"
            elif(self.codons[i] == GCU or GCC or GCA or GCG):
                self.protein[i] = "  Ala  ,"
            elif(self.codons[i] == UAU or UAC):
                self.protein[i] = "  Tyr  ,"
            elif(self.codons[i] == UAA or UAG):
                self.protein[i] = "  STOP  ,"
            elif(self.codons[i] == CAU or CAC):
                self.protein[i] = "  His  ,"
            elif(self.codons[i] == CAA or CAG):
                self.protein[i] = "  Gln  ,"
            elif(self.codons[i] == AAU or AAC):
                self.protein[i] = "  Asn  ,"
            elif(self.codons[i] == AAA or AAG):
                self.protein[i] = "  Lys  ,"
            elif(self.codons[i] == GAU or GAC):
                self.protein[i] = "  Asp  ,"
            elif(self.codons[i] == GAA or GAG):
                self.protein[i] = "  Glu  ,"
            elif(self.codons[i] == UGU or UGC):
                self.protein[i] = "  Cys  ,"
            elif(self.codons[i] == UGG):
                self.protein[i] = "  Trp  ,"
            elif(self.codons[i] == CGU or CGC or CGA or CGG):
                self.protein[i] = "  Arg  ,"
            elif(self.codons[i] == GGU or GGC or GGA or GGG):
                self.protein[i] = "  Gly  ,"
            else:
                self.protein[i] = "  RRR  ,"

        return self.protein


#One method to rule them all
    def do_all_translator(self):
        self.reformed = check_string(self, string_RNA)
        self.codons = find_codons(self, reformed)
        self.protein = translator (self, codons)
        return self.protein





#-----------------------------------------------class end-------------------------------------










