 #! /usr/bin/python

import os

from configparser import ConfigParser

if __name__ == "__main__":
    cfg = ConfigParser()

    cfg.read('config1.txt')
    PrintPath = cfg.get('PrintJobConfig', 'print_path')
    JobNum = int(cfg.get('Test_Setting', 'job_num'))
    i=0

    # Basic print job

    for i in range(0,JobNum):
     os.startfile(PrintPath, "print")



"""
    # Code to add widgets will go here...
    with open('config1.txt', 'w') as configfile:
            cfg.write(configfile)

    configParser1=ConfigParser
    configFilePath= r'C:/Users/Yang Tao/Desktop/'
    configParser1.read(configFilePath,'config.txt')

    parameter1=configParser.get('config1','parameter1')
    print(parameter1)
"""
"""
    print(cfg.sections())  # return all sections
    print(cfg.items('PrintJobConfig'))  # return section's list
    print(cfg.get('PrintJobConfig', 'User_num'))
    print(cfg.get('PrintJobConfig', 'Job_num'))
    print(cfg.get('PrintJobConfig', 'print_format'))

    cfg['PrintJobConfig'] = {'User_num': '1', 'Job_num': '10', 'Print_format': 'text'}
        cfg['Server Info'] = {}
        cfg['Server Info']['IP'] = '192.168.12.159'  # set "string"
        cfg['Server Info']['Domain'] = 'Jetmobiledemo\jetmobile'  #set "string"
        cfg['Server Info']['Gateway'] = '255.255.255.125'  # set "string"
        cfg['Server Info']['Connection'] = 'True'  # set "bool"
"""


