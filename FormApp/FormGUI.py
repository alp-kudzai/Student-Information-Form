#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:28:50 5021

@author: Kudzai Matsika alpha.kudzai@gmail.com
"""
from baseClasses import *
import PySimpleGUI as sg
group_id = 'PRC'

def FileName(name):
    filename = name+'.txt'
    return filename

def buildForm(values, studentForm, full_name, Storage):
    listOfilled = [values['BRTH'], values['P1FN'], values['P1CN'], 
                   values['P2FN'], values['P2CN'],values['SK'], 
                   values['FAM'], values['HL'], values['FF'], values['FC'], values['PA']
                   ]
    form_field = ['Birthday', 'Parent1', 'Parent2', 'Parent1 Numbers', 
                  'Parent2 Numbers', 'Skills', 'Ambitions', 'Hobbies',
                  'Fav Food', 'Fav Colour', 'Physical Address']
    # print(values['PA'], values['FC'])
    for i in range(len(listOfilled)):
        studentForm.set_STUDinfo(form_field[i], listOfilled[i])
    Storage.addToStore(full_name, studentForm)
    return Storage

def updatebuild(values, studentForm, full_name, Storage):
    keys = ['BRTH', 'P1FN', 'P1CN', 'P2FN', 'P2CN', 'SK', 'FAM', 'HL', 'FF',
            'FC', 'PA']
    listOfilled = []
    for k in keys:
        if len(values[k]) > 0:
            listOfilled.append(values[k])
    # print(listOfilled)
    form_field = ['Birthday', 'Parent1', 'Parent2', 'Parent1 Numbers', 
                  'Parent2 Numbers', 'Skills', 'Ambitions', 'Hobbies',
                  'Fav Food', 'Fav Colour', 'Physical Address']
    for i in range(len(listOfilled)):
        Storage.update_STUDinfo(full_name,form_field[i], listOfilled[i])
    return Storage
    

column1 =[[sg.Text('*Student Full Name', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10), tooltip='If updating a student info, double-check student name spelling')],
          [sg.Txt('Birthday', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
          [sg.Txt('Parent Full Name', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
          [sg.Txt('Parent Contact Numbers', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
          [sg.Txt('2nd Parent Full Name', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
          [sg.Txt('2nd Parent Contact Numbers', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
          [sg.Txt('Physical Address', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
          [sg.Txt('Favourite Colour', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
          [sg.Txt('Favourite Food', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
          [sg.Txt('Hobbies List', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
          [sg.Txt('Future Ambitions', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
          [sg.Txt('Skills', text_color='brown', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))]
          
]
column2 = [[sg.Input('', size=(50,1), key='SFNAME')],
           [sg.Input('', size=(50,1), key='BRTH')],
           [sg.Input('', size=(50,1), key='P1FN')],
           [sg.Input('', size=(50,1), key='P1CN')],
           [sg.Input('', size=(50,1), key='P2FN')],
           [sg.Input('', size=(50,1), key='P2CN')],
           [sg.Input('', size=(50,1), key='PA')],
           [sg.Input('', size=(50,1), key='FC')],
           [sg.Input('', size=(50,1), key='FF')],
           [sg.Input('', size=(50,1), key='HL')],
           [sg.Input('', size=(50,1), key='FAM')],
           [sg.Input('', size=(50,1), key='SK')]
           
    ]

layout = [[sg.Text('Student Information Form.', 
                   size=(50, 2), justification='center', 
                   font=("Helvetica", 20), relief=sg.RELIEF_RIDGE, key='TOP')],
         #---------Student Info form--------------------------------# 
          [sg.Frame(layout=[ [sg.Column(column1, justification='center', element_justification='center'), sg.Column(column2, justification='center', element_justification='center')],
          [sg.Submit(), sg.Button('Update Student')]], title='Form', title_color='brown', 
              relief=sg.RELIEF_SUNKEN, tooltip='The name is required; Fill form with as much info as possible.')],
          #-----------------Program commands-----------------------
          [sg.Frame(title='Program Commands',layout=[[sg.Radio('Get Student Info', group_id, enable_events=True, tooltip='Enter Student Full Name Below', key='GETSI'), 
                             sg.Radio('Remove Student from Database', group_id, enable_events=True, tooltip='Enter Student Full Name To Be Removed', key='RS')]])],
          [sg.Input('Enter student name', size=(20,1), do_not_clear=True, focus=True, key='NAME'), sg.Button('Ok', focus=True)],
          [sg.Text('Save/Load', size=(8, 1), relief=sg.RELIEF_RIDGE, font=('Helvetica', 10)), sg.Input(key='FILE', tooltip='If saving, just enter the filename you want it saved as.'), sg.FileBrowse()],
          [sg.Button('Load', tooltip='Fist Browse to find your folder, then load', focus=True), sg.Button('Save', tooltip='Fist Browse to find a folder to save to, then save', focus=True)],
          [sg.Button('EXIT', tooltip='Save before exiting please!!', focus=True)]
    ]
sg.theme('NeutralBlue')
window = sg.Window('Student Information Forms', layout, default_element_size=(40, 1), grab_anywhere=False, element_justification='center',background_color='#6a8d92')
SStorage = INFO_STORE()
while True:
    event, values = window.read()
    try:
        if event in ('EXIT', None) or event == sg.WIN_CLOSED:
            break
        if event == 'Submit' and len(values['SFNAME']) > 0:
            studentForm = Student()
            stud_name = values['SFNAME']
            SStorage = buildForm(values, studentForm, stud_name, SStorage)
            sg.popup(SStorage.get_STUDinfo(stud_name), title=stud_name)
        elif event == 'Update Student' and len(values['SFNAME']) > 0:
            studentForm = Student()
            stud_name = values['SFNAME']
            SStorage = updatebuild(values, studentForm, stud_name, SStorage)
            sg.popup(SStorage.get_STUDinfo(stud_name), title=stud_name)
        elif (values['GETSI']) and (event == 'Ok') and (len(values['NAME']) > 0):
            stud_name = values['NAME']
            sg.popup(SStorage.get_STUDinfo(stud_name), title=stud_name)
        elif (values['RS']) and (event == 'Ok') and (len(values['NAME']) > 0):
           stud_name = values['NAME']
           SStorage.RM_STUD(stud_name)
           sg.popup(f'{stud_name} has been deleted from database', title='DELETED')
        elif event =='Load' and len(values['FILE']) > 0:
            infile = values['FILE']
            SStorage.load_StudentData(infile)
            sg.popup('Data loaded', title='Loading File')
        elif event == 'Save' and len(values['FILE']) > 0:
            outfile = values['FILE']
            SStorage.save_StudentData(outfile)
            sg.popup('Data saved', title='Saving File')
    except:
        sg.popup(f'Something Went Wrong\n{event}\nvalues: {values}',title='ERROR Handler')
        
window.close()






   