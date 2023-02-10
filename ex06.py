# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 01:36:02 2023

@author: serdna
"""

cookbook = {
    "Sandwich":{
       "Ingredients": ["ham", "bread", "cheese", "tomatoes"],
       "meal": "lunch",
       "prep_time": "10 minutes"
       },
    "cake":{
       "Ingredients":["flour", "sugar","eggs"],
       "meal": "dessert ",
       "prep_time": "60 minutes"
       },
    "salad":{
       "Ingredients":["avocado", "arugula", "tomatoes", "spinach"],
       "meal": "lunch",
       "prep_time": "15 minutes"
       }
}

#https://www.tutorialspoint.com/How-to-print-all-the-keys-of-a-dictionary-in-Python
#https://www.delftstack.com/es/howto/python/nested-dictionary-python/

def print_name():
    for key, value in  cookbook.items():
        print (key)

def print_ingredients(str):
    for key, value in  cookbook.items():
        if str == key:
            print(f'Ingredients list: {cookbook[str]["Ingredients"]}')
            print (f'To be eaten for {cookbook[str]["meal"]}♥')
            print (f'Takes {cookbook[str]["prep_time"]} of cooking.')
            
 
def delete_dict(str):
    if str in cookbook:
        del cookbook[str]
        print("Delete completed")

def add_dict(name, list_element, time, type_):
    
    cookbook.update({name:{'Ingredients':list_element, "meal":type_, "prep_time":time}})

  
def menu():
    print("Welcome to the Python Cookbook !")
    print("List of available option:\n")
    print("1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")
    select = input("Please select an option:\n >> ").lower()
    try:
        while (select != "5"):
            if select == "1":
                name = input("name :\n >>")
                list_element = list(input("elements :\n >>").split(" "))
                time = input("Time only time in munutes :\n >>")
                type_ = input("Type meal? :\n >>")
                add_dict(name, list_element, time, type_)
            elif select == "2":
                str = input("QUe quieres borrar? nombre? :\n >> ")
                delete_dict(str)
            elif (select == "3"):
                str = input("nombre receta?? :\n >> ")
                print_ingredients(str)
            elif (select == "4"):
                print_name()
            select = input("Please select an option:\n >> ").lower()
    except KeyboardInterrupt:
        print('Hello user you have pressed ctrl-c button.')
    except:
        print("Algo ha ido mal y no ha sido culpa mia... echale la culpa al que esta a tu lado")
    print("Cookbook closed. Goodbye !")
#add_dict("azucar", ["uno", "dos", "tres"], "40 minutos", "lnuch")

menu()


