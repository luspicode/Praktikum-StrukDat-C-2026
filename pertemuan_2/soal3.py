tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

#1. tentukan irisannya 
irisan = tim_frontend.intersection(tim_backend)
print (irisan)

#2. yang hanya ada di backend
backendaja = tim_backend.difference(tim_frontend)
print (backendaja)

#3. gabungkan keduanya
gabungan = tim_frontend.union(tim_backend)
print (gabungan)
