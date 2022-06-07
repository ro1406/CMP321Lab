# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 00:32:17 2022

@author: rohan
"""
serverInfo = ( "id=0;role=admin;username=joe;surname=naysmith", 
                         "surname=suffi;username=sam;role=guest;id=421",
                        "id=33;surname=lee;username=mia;role=staff"  )
#a)
database={}

for record in serverInfo:
    fields=record.split(';')
    fields=sorted(fields,reverse=True)
    #ID is not always the first element, so must find it:
    for field in fields:
        if 'id=' in field:
            #Found the id field!
            currID=field.split('=')[1] #Store the ID
            fields.remove(field) #Dont need it in the array anymore
            break

    innerDict={} # The record for each ID
    for field in fields:
        innerDict[field.split('=')[0]]=field.split('=')[1]
    
    database[currID]=innerDict

for key in sorted(database.keys()):
    print(key,"   ",database[key])
    
    
#b)
for key in sorted(database.keys()):
    record=database[key]
    print(f"{record['surname'].title()}, {record['username'].title()} - {record['role']}")