#Del 1 af øvelse 1
"""
# Variabel
float1 = 73.33
#Typecasting til integer med en ny variabel
resultat = int(float1)
#print resultatet ud
print(resultat)
#se typen
print("se type: ", type(resultat))
"""

#Øvelse 1
"""
 # Her er opgaverns varibalere i flydende værdi (float decimaltal)
float1 = 5799.7345

float2 = 1111.1111

float3 = 339.993

float4 = 1.0
# Her fortæller jeg at det skal være int numre (heltal)
resultat = int(float1)
print(resultat) #Her får jeg printet resultatet
print("se type: ", type(resultat)) #Her kan vi se type i Int (Heltal)

resultat = int(float2)
print(resultat)
print("se type: ", type(resultat))

resultat = int(float3)
print(resultat)
print("se type: ", type(resultat))

resultat = int(float4)
print(resultat)
print("se type: ", type(resultat))
"""

"""
#Øvelse 2 del 1
#Variabel
int1 = 9784
#typecasting til en ny variabel
resultat = float(int1)
#print resultatet ud
print(resultat)
"""
"""
#Øvelse 2. 
int1 = 5787 # Opgavens variabler i int(heltal)

int2 = 1

int3 = 255

int4 = 445

resultat = float(int1) #Her beder vi om at det bliver udskrevet i float
print(resultat) #Printer resultatet.

resultat = float(int2)
print(resultat)

resultat = float(int3)
print(resultat)

resultat = float(int4)

print(resultat)
"""
"""
#Øvelse 3 del 1
 # variabel
string1 = "4344"
 # typecasting til en ny variabel
resultat = int(string1)
 # print resultatet ud
print(resultat)

"""

"""
#Øvelse 3
string1 = "255" #Hver string er variablen for en teskt.
resultat = int(string1) #Udregner det til int(heltal)
print(resultat) #Printer resultatet i shell.
string2 = "1"
resultat = int(string2)
print(resultat)
string3 = "1023"
resultat = int(string3)
print(resultat)
string4 = "127"
resultat = int(string4)
print(resultat)
"""
"""
#Øvelse 4
# Hver butik har fået et tal, og hvad deres besøgende kunder var
# Den 3.August.
butik1 = "129"
butik1_in = int(butik1) # Ville gerne have alle besøgende i Int værdi.

butik2 = 143
butik2_in = int(butik2)

butik3 = 233.0
butik3_in = int(butik3)

butik4 = "98"
butik4_in = int(butik4)

butik5 = 86.0
butik5_in = int(butik5)

# Lægger alle variablerne sammen som nu er heltal.
resultat = int(butik1_in + butik2_in + butik3_in + butik4_in + butik5_in)

print(resultat) #Printer resultatet.
"""

"""
#Øvelse 5
# Temperaturmålinger fra de fem målningsstationer
temperaturer = [21.2, 20.5, 21.6, 22.1, 21.5]

# Beregning af gennemsnittet
gennemsnit = sum(temperaturer) / len(temperaturer)

# Udskriv gennemsnittet med én decimal
print(f"Gennemsnitlig temperatur: {gennemsnit:.1f}°C")
"""

"""
#Øvelse 7.1
class Person:
    navn = ""
    alder = 0
    land = ""

    def beskrivelse(self):
        print(f"Hej, Jeg hedder {self.navn} og jeg er {self.alder} år gammel, og kommer fra {self.land}.")

# Instanser af klassen Person
person0 = Person()
person0.navn = "Magnus"
person0.alder = 21
person0.land = "Danmark"
person0.beskrivelse()

person1 = Person()
person1.navn = "Josephine"
person1.alder = 20
person1.land = "Danmark"
person1.beskrivelse()

person2 = Person()
person2.navn = "Lucas"
person2.alder = 23
person2.land = "Danmark"
person2.beskrivelse()
"""
"""
#Øvelse 7.4
class Person():
    def __init__(self, navn, alder, land):
        self.navn = navn
        self.age = alder
        self.land = land
    
    # Det er vigtigt at def er på samme linje start.
    def beskrivelse(self):
        print("%s is %d years old and he is from %s." % (self.navn, self.age, self.land))

# Det her fortæller om person1.
person1 = Person("Magnus", 25, "Danmark")

# Det her er til at få det hele printet sammen.
person1.beskrivelse()
"""


        
        






