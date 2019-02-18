# -*- coding:utf-8 -*-
from os.path import exists
class FileManager():
    def __init__(self):
        print "welcome to file manager..."
        print "press to copy data file[1]: "
        print "press to delet the file[2]: "
        print "perss to change path[3]"
        print "press to show file data[4]: "
        print "press to longth of data[5]: "
        self.chooses()

    def chooses(self):
        while True:
            user_choose = raw_input('> ')
            user_choose = user_choose.lower()
            if user_choose == "quit":
                break
            try:
                user_choose = int(user_choose)
                if user_choose == 1:
                    self.__copy__()
                
                elif user_choose == 2:
                    self.__delat__()
                
                elif user_choose == 3:
                    self.__changepath__()
                
                elif user_choose == 4:
                    self.__showdata__()
                
                elif user_choose == 5:
                    self.__datalen__()
                else:
                    print "pleas choos number from 1 to 4 or [quit to exit]"
            except ValueError:
                print "Pleas enter a valid number(*_*)"

    def __copy__(self):
        areyouwant = raw_input("do you want to copy files data [Y,N]? ")
        areyouwant = areyouwant.lower()
        if areyouwant == 'y':
            while True:
                filename = raw_input('input the full path of file: ')
                is_exists = exists(filename)
                if is_exists:
                    pass
                else:
                    filename = filename.lower()
                
                if is_exists:
                    filedist = raw_input('input the full path of distnation: ')
                    openfile = open(filename)
                    datafile = openfile.read()

                    opendist = open(filedist,'a')
                    writeondist = opendist.write('\n' + datafile)
                    
                    opendist.close()
                    openfile.close()

                    print "Copied Successfully!!!"
                elif filename == 'quit':
                    break
                else:
                    print "Pleas enter the full path agin"
        else:
            print "thanks..."



    def __delat__(self):
        import os
        while True:
            filename = raw_input('input the full path of file you want to remove: ')
            is_exists = exists(filename)
            if is_exists:
                pass
            else:
                filename = filename.lower()
            
            if filename == 'quit' and not is_exists:
                break
            elif is_exists:
                sur = raw_input('are you suer you want remove[Y,N]??')
                sur = sur.lower()
                if sur == 'y':
                    os.remove(filename)
                else:
                    break
            else:
                print "Pleas try agin"

    def __changepath__(self):
        pass

   def __showdata__(self):
        while True:
            filename = raw_input('Enter the full path of file: ')
            is_exists = exists(filename)
            if is_exists:
                pass
            else:
                filename = filename.lower()
            
            if filename == 'quit' and not is_exists:
                break
            elif is_exists:
                openfile = open(filename)
                data = openfile.read()
                print data + '\n \n completed successfully!!! '
            else:
                print "Pleas enter the path agin."

    def __datalen__(self):
        while True:
            filename = raw_input('Enter the full path of file: ')
            is_exists = exists(filename)
            if is_exists:
                pass
            else:
                filename = filename.lower()
            print "This file is exists? %s" % is_exists
            if is_exists:
                openfile = open(filename)
                data = openfile.read()
                print len(data)
                print '\nSuccessfully Completed!!!'
            elif filename == 'quit' and not is_exists:
                break
            else:
                print "Pleas enter the file name agin"
