a = "21.2"
b = "20.5"
c = "21.6"
d = "22.1"
e = "21.5"
#initialiserer 5 strings

x = float(a)+float(b)+float(c)+float(d)+float(e)
#laver en x-variabel og tildeler den strings efter de er konverteret til floats

y = x/5
# laver en y variabel, som er summen/gennemsnittet af alle værdierne kl. 18
print(y)

svar = f"gennemsnitstemperaturen kl 18:00 er {y:.1f}"
# laver en f string som bruges til at printe svaret samt en forklaring.
#{y:.1f}, indregner 1 decimal. y er funktionen, og .1f indregner 1 decimal,
#hvor at f er float

print(svar)
