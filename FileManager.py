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
                