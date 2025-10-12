# lets a create a dictionary.
student_results = {
    "Maths_marks": {
          "Samuel" : 89 ,
          "Josephine" : 78 ,
          "Katherine" : 99 ,
          "Mehmet" : 90 ,
          "Ahaan" : 77 ,

    },
    
    "English_marks" : {
        "Samuel" : 98 ,
        "Josephine" : 99 ,
        "Katherine" : 88 ,
        "Mehmet" : 95 ,
        "Ahaan" : 98 ,


    } ,
}
print(student_results)

Annual_report ={
    "Students" : "five-students" ,
    "Examination" : ["Math_exam" , "English_exam"],

}
print(Annual_report)

# Spareparts exclusive store.

store_stored ={}

x = int(input("How many spark plugs:"))
store_stored.update ({"spark-plugs" : x})

x = int(input("How many Engine Oil Filters:"))
store_stored.update ({"Engine Oil Filters" : x})

x = int(input("How many Brake Pads:"))
store_stored.update ({"Brake Pads" : x})

x = int(input("How many Headlight Bulbs:"))
store_stored.update ({"Headlight Bulbs" : x})

x = int(input("How many Air Filters:"))
store_stored.update ({"Air Filters" : x})

print(store_stored) 

# Store 9 and 9.0 seperately

values = {
    ('float' , 9.0),
    ('int' , 9)
}
print(values)
