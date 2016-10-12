 #! /usr/bin/python

import os
import time
import threading
from configparser import ConfigParser


class myThread (threading.Thread):
    def __init__(self, threadID, name, jobnum, path, usernum ):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.jobnum = jobnum
        self.usernum = usernum
        self.path = path
    def run(self):
        print ("Starting " + self.name)
        Print_Per_User(self.jobnum,self.path,self.usernum)
        print ("Exiting " + self.name)

#Define a function which can print Jobnum's print job
def Print_Per_User(jobnum, path, usernum):
    for i in range(0,jobnum):
    # For testing use print only
      localtime = time.asctime(time.localtime(time.time()))
      print( localtime," -----User={}, Job number= {}".format(usernum,jobnum) )
    #accutal testing print the job
      #os.startfile(PrintPath, "print")

def Print_User(jobnum, path, usernum):
    for i in range (0,usernum):
        try:
            #Print_Per_User(jobnum,path,usernum)  #("Thread" + str(i), i,))
            thread1 = myThread(i+1, "Thread"+str(i+1), jobnum, path, i+1)
           # print("Start Thread {}".format(i+1))
            thread1.start()
        except:
            print ("Error: unable to start thread")


if __name__ == "__main__":
    cfg = ConfigParser()

    cfg.read('config1.txt')
    PrintPath = cfg.get('PrintJobConfig', 'print_path')
    JobNum = int(cfg.get('PrintJobConfig', 'job_num'))
    UserNum = int(cfg.get('PrintJobConfig', 'user_num'))
    i=0
    Print_User(JobNum,PrintPath,UserNum)





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


