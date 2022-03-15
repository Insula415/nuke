#!/usr/bin/python3
import os 
from os import path
from time import sleep
import sys
import shutil


folder = "" #put folder path here

opt = input("Are you sure you want to do this...? ")
x = ["y", "yes"]

running = True
count = 1

def tryagain(running = True):
    count = 1
    x = ["y", "yes"]
    while running:
        newpath = input("Enter path: ")
        if path.exists(newpath):
            option = input("This path exists. Are you sure you want to do this? ")
            if option in x:
                while count <=5:
                    print("Removing",newpath,"in",count)
                    count += 1
                    sleep(1)
                try:
                    shutil.rmtree(newpath)
                    running = False
                except:
                    print("Something went wrong...")
                    print(" ")
        else:
            print(newpath,"does not exist")
            

def randError():
    x = ["y", "yes"]
    option = input("Would you like to manually input a folder path? ")
    if option in x:
        print(tryagain())
    else:
        print("Until next time.")

if opt in x:
    if path.exists(folder):    
        try:
            while count <= 5:
                print("Removing",folder,"in",count)
                sleep(1)
                count += 1
            shutil.rmtree(folder)
            print("Nothing ever happened.")

        except OSError as e:
            print("Error: %s does not exist" % e.filename)
            print(randError())

    else:
        print(folder,"does not exist")
        print(randError())
