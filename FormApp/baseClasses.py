#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 08:57:16 2021

@author: User
"""
# from time import *
import pickle
#classes for student forms
#Things on the form:
    #Full Name
    #Birthday
    #Parent1 Full Name
    #Parent2 Full Name
    #Contact number/s
    #fav colour
    #fav food
    #physical address
    #hobbies
    #ambitions
    #skills
#Plan: Make a class for 1 student, this class takes info
      #about the student.
      
      #Then we have another class that takes in each student
      #class and stores the information and can retrive it
      #when asked
      
# BIN: birthday=None, parent1_contact=None, 
#                  parent2_contact=None, parent1=None, parent2=None,
#                  skills=None, ambitions=None, hobbies=None, fav_food=None,
#                  fav_color=None,physical_address=None
      
dict_info = ('Birthday','Parent1', 'Parent2', 'Parent1 Numbers',
             'Parent2 Numbers', 'Skills', 'Ambitions', 'Hobbies',
             'Fav Food','Fav Colour' 'Physical Address')
      
class Student(object):
    def __init__(self):
        self.STUDinfo = { 'Birthday': None,
                          'Parent1': None,
                          'Parent2': None,
                          'Parent1 Numbers': None,
                          'Parent2 Numbers': None,
                          'Skills': None,
                          'Ambitions': None,
                          'Hobbies': None,
                          'Fav Food': None,
                          'Fav Colour': None,
                          'Physical Address': None}
        
    def getAll_info(self):
        stud_info = self.STUDinfo.items()
        res = '-----Student Information-----\n'
        for info in stud_info:
            # print(info[0],info[1])
            if not info[1]==None:
                res += f'{info[0]}-----------------{info[1]}\n'
            else:
                res += f'{info[0]}-----------------N/A\n'
        return res[:-1]
    
    def getSpecific(self, item):
        try:
            res = f'{item}: {self.STUDinfo[item]}'
        except:
            res =f'ERROR:{item} is not part of the stored information!'
        finally:
            return res
        
    def rm_info(self, category):
        try:
            self.STUDinfo[category] = None
            return f'{category} removed'
        except:
            return f'Error removing {category}'
        
    def update_info(self, category, new_info):
        try:
            self.STUDinfo[category] = new_info
            return f'{category} has been updated'
        except:
            return f'ERROR: {category} doesnt exist!'
    
    #Set can also update info
    def set_STUDinfo(self, category, info):
        # print(category, info)
        if len(info) > 0:
            self.STUDinfo[category] = info
        else:
            return f'ERROR: {category} does not exist as a category!'
# if category in dict_info:
    
class INFO_STORE(object):
    def __init__(self):
        self.Ult_storage = {}
    #addToStore can also update info    
    def addToStore(self, student_name, student_info):
        try:
            if student_name in self.Ult_storage:
                self.Ult_storage[student_name] = student_info
                return f'{student_name} Updated!'
            else:
                self.Ult_storage[student_name] = student_info
                return f'{student_name} stored'
        except:
            return f'ERROR: Could not store {student_name}'
        
    def RM_STUD(self, student_name):
        try:
            self.Ult_storage.pop(student_name)
            return f'{student_name} has been removed.'
        except:
            f'ERROR: Could not remove {student_name}'
        
    def rm_STUDinfo(self, student_name, category):
        return self.Ult_storage[student_name].rm_info(category)
    
    def update_STUDinfo(self, student_name, category, new_info):
        if student_name in self.Ult_storage:
            return self.Ult_storage[student_name].update_info(category, new_info)
        else:
            return f'ERROR: {student_name} not in storage'
        
    def get_STUDinfo(self, student_name, specific_info=None):
        if student_name in self.Ult_storage:
            if specific_info == None:
                return self.Ult_storage[student_name].getAll_info()
            elif specific_info in dict_info: #im checking in dict_info twice; can be rempved
                return self.Ult_storage[student_name].getSpecific(specific_info)
            else:
                return f'ERROR: Could not find {student_name} or specified information!'
            
    def load_StudentData(self, filename):
        try:
            infile = open(filename, 'rb')
            print(f'Loading Pickled Data from {filename}....')
            self.Ult_storage = pickle.load(infile)
            infile.close()
            print('Data Loaded!')
        except:
            print(f'ERROR: Could not load data from {filename}!')
        
    def save_StudentData(self, filename):
        try:
            outfile = open(filename, 'wb')
            print(f'Saving data to {filename}')
            pickle.dump(self.Ult_storage, outfile)
            outfile.close()
            print('Data saved!')
        except:
            print(f'ERROR: Could not save data to {filename}!')
            
            
        
            
        
        
        
        