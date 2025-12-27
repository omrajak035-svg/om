info ={
    "key":"value",
    "name" :  "om",
    "learning":"coding",
    " age" : "19",
    12.33 : 11.33
}
info["name"] = "ohm"
info ["surname"] = "rajak"
print(info)

student = {
"name" : "abhyam",
"subject" : {
    "business communication" : 23 ,
    "BE" : 26 , 
    "FOM" : 14 ,
    "EVS" : 12,
    "MOM" : 24
    
    }
}

print(student["subject"]["BE"])

dis = {
    "a" : "s",
    "f" : "e",
    "sub" : {
        "alu" : 34,
        "bhalu" : 34,
        "chalu" : 83
             
    }
}

print(len(list(dis.keys())))


collection = { 1 , 1 ,2 , 3 , 4 , 5 , 5 , 5}
print(collection)

print(type(collection))
print (len(collection))
collection.add(6)
collection.remove(3)
print(collection)

set1 = { 1,2 ,3}
set2 = { 2 , 3, 4}
print(set1.union(set2))

set3 = { 1,2 ,3}
set4 = { 2 , 3, 4}
print(set3.intersection(set4))