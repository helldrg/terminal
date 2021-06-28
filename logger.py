# print all 
from typing import Text
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
from PyQt5.QtCore import (Qt, QDate, QTime, QDateTime)
import xml.etree.ElementTree 
import os
  
class Logger:
    file = 'log.xml'
    count = 0
    lastId = 0
    def __init__(self):
        pass

    def open_xml(self) :
        if os.path.isfile(self.file) == False:
            self.create_xml()
        else:
            #TODO: rechange logic
            try:
                tree = xml.etree.ElementTree.parse(self.file)
                root = tree.getroot()
            except Exception:
                os.remove(self.file)
                self.create_xml()
            
                tree = xml.etree.ElementTree.parse(self.file)
                root = tree.getroot()

            self.count = int(root.get("lastId"))
            self.lastId = int(root.get("count"))

    def genrate_xml(self):
        root = Element("Logger")
        root.set('version', '1.0')
        root.set("count", str(self.count))
        root.set("lastId", str(self.lastId))
        root.append(Comment('Generated xml file'))
        #ET.SubElement(doc, "field1", name="blah").text = "some value1"
        '''
        for i in range(2):
            log = SubElement(root, "Log")
            #log = Element("Log")
            #root.append (log)
            id = SubElement(log, "id")
            id.text = "0"
            time = SubElement(log, "time")
            time.text = "6999"
            action = SubElement(log, "action")
            action.text = "new device"
            description = SubElement(log, "description")
            description.text = "создание нового устройства"
            self.count += 1
            root.set("count", str(self.count))
        '''
        return ElementTree(root)

    def create_xml(self):
        tree = self.genrate_xml()
        try:
            with open (self.file, "wb") as files:
                tree.write(files)
        except Exception:
            #TODO: print message in status bar
            print('Создать файл с логами не удалось')
            assert False, 'Не удалось создать файл'


    def addElement(self, act):
        tree = xml.etree.ElementTree.parse(self.file)
        root = tree.getroot()

        log = SubElement(root, "Log")

        id = SubElement(log, "id")
        id.text = str(self.lastId)
        timespan = SubElement(log, "time")
        date = QDate.currentDate()
        time = QTime.currentTime()
        timespan.text = date.toString(Qt.ISODate) + " : " + time.toString(Qt.DefaultLocaleLongDate)
        action = SubElement(log, "action")
        action.text = act
        description = SubElement(log, "description")
        description.text = "empty"

        self.count += 1
        self.lastId += 1
        root.set("count", str(self.count))
        root.set("lastId", str(self.lastId))

        tree = ElementTree(root)

        with open (self.file, "wb") as files:
            tree.write(files)

    def printElemets(self):
        tree = xml.etree.ElementTree.parse(self.file)
        root = tree.getroot()

        # all items data
        print('\nAll item data:')
        for elem in root:
            for subelem in elem:
                print(str(subelem.tag) + " = " +  str(subelem.text))

    def findElementsId(self, id):
        pass

    def countElements(self):
        tree = xml.etree.ElementTree.parse(self.file)
        root = tree.getroot()
        print(len(root[0]))
  
# Driver Code
if __name__ == "__main__": 
    Logger = Logger()
    Logger.open_xml()
    Logger.addElement("add")
    Logger.addElement("in")

    Logger.printElemets()