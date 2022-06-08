# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 00:32:17 2022

@author: rohan
"""
serverInfo = ( "id=0;role=admin;username=joe;surname=naysmith", 
                         "surname=suffi;username=sam;role=guest;id=421",
                        "id=33;surname=lee;username=mia;role=staff"  )
#a)
def makeDatabase():
    database={}
    
    for record in serverInfo: 
        fields=record.split(';')
        fields=sorted(fields,reverse=True)
        
        currID=fields[-1].split('=')[1] #The last field is the ID (since we sorted in descending order)
    
        innerDict={} # The record for each ID
        for field in fields[:-1]:#Omit the ID
            innerDict[field.split('=')[0]]=field.split('=')[1]
        
        database[currID]=innerDict
    return database

db=makeDatabase()
print('db =',db)
    
    
#b)
for key in sorted(db.keys()):
    record=db[key]
    print(f"{record['surname'].title()}, {record['username'].title()} - {record['role']}")