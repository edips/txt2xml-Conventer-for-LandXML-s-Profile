import csv
print("----------------------------------------------------------------")
print("""Bu script NetCAD KTB'ten LandXML'e dusey guzergah parametrelerini olusturur.
NetCAD'ten yatay guzergah DXF olarak kaydedilip Inroads veya Civil3D'de LandXML
guzergah dosyasina cevrilir ve dosya kaydedilir. """)
print("NetCAD KTB dosyasini acin. $DUSEY ve $SON arasindaki degerleri text dosyasi \n olarak scriptin oldugu klasore kaydedin.")
print()
print("----------------------------------------------------------------")
a=input("Text dosya adi: ")
dusey=input("Dusey guzergah adi: ")
print("----------------------------------------------------------------")
f = open(a)
csv_f = csv.reader(f)
#-----------------------------------------------------
k = []
data2=[]
for row in csv_f:
    data2.append(row)
  
for i in data2:
    for a in i:
        a=a.split()
        k.append(a)
data=[]

for i in k:
    data.append(i[:-1])
f.close()    
#-------------------------------------------------------------------
x=data[0][0]
y=data[0][1]

a=data[-1][0]
b=data[-1][1]

def convert_row(row):
    return """
       <ParaCurve length="%s">
           %s %s
        </ParaCurve>
""" % ( row[2], row[0],row[1])
   #"<ProfAlign name = 'hv'>"'\n' + \
xml="<Profile>" '\n'+ \
   "<ProfAlign name = "+'"'+dusey+'"'+">"'\n' + \
   "   <PVI>"'\n' +  \
   "      %s %s"%(x,y)+  \
       '\n'"</PVI>" + \
        "".join([convert_row(row) for row in data[1:-1]])+  \
       "    <PVI>"'\n'+ \
       "      %s %s"%(a,b)+ \
       '\n'"      </PVI>"'\n'+ \
       "</ProfAlign>"'\n'+ \
       "</Profile>"

with open('vertical_alignment.txt', 'w') as f:
   f.write(xml)
print()   
print("LandXML icin dusey guzergah parametreleri 'vertical_alignment.txt' olarak kaydedildi.")
print("""Dosya icerigini kopyalayin ve yatay guzergah olarak kaydedilen LandXML dosyasini acip </CoordGeom> ile <Feature code='Alignment'> arasina kaydedin. Islem sonucu yatay ve dusey geometri LandXML olarak hazir.""")
print("Programmed by Edip Ahmet TASKIN")
print("----------------------------------------------------------------")
print()
print(input("Press enter to exit.."))
