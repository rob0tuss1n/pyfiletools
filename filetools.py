from datetime import date, datetime
import os

class log():
	def __init__(self,name,path="",tFormat="datetime"):
		self.name = name
		if os.path.exists(path):
			self.path = path
		else:
			self.path = os.getcwd()
		self.filePath = self.path + self.name
		if tFormat == "datetime":
			self.timeFormat = "datetime"
		elif tFormat == "date":
			self.timeFormat = "date"
		else:
			self.timeFormat = "datetime"
	
	def addLog(self,s):
		filePath = self.path+self.name
		if self.timeFormat=="datetime":
			entry = str(datetime.now())+str(" "+s+" ")+'\r\n'
		if self.timeFormat=="date":
			entry = str(date.today())+str(" "+s+" ")+'\r\n'
		self.file = open(self.filePath, 'a')
		self.file.write(entry)
		self.file.close()
		return entry
		
	def readLogFile(self):
		self.file = open(self.filePath, 'r')
		contents = self.file.read()
		self.file.close()
		return contents
	
	def lineCount(self):
		try:
			self.file = open(self.filePath, 'r')
			lines = sum(1 for line in self.file)
			self.file.close()
		except IOError:
			lines = 0
		return lines
	
	def changeFileName(self,name,path=""):
		currentName = self.filePath
		if len(path) > 0 and os.path.exists(path):
			fullName = path + name
		else:
			fullName = self.path + name
		print name
		self.file.close()
		try:
			os.rename(currentName,fullName)
			self.name = name
			self.filePath = fullName
		except OSError:
			print 'A file with the name ' + str(name) + ' already exists'
		except:
			print "Unknown Error!!! Unable to rename file."
		
	def changeTimeFormat(self,tFormat):
		if tFormat == "datetime":
			self.timeFormat = "datetime"
			message = "Time Format Changed"
		elif tFormat == "date":
			self.timeFormat = "date"
			message = "Time Format Changed"
		else:
			self.timeFormat = "datetime"
			message = "Bad Time Format Entry"
		return message

class pCSV():
	def __init__(self,name,path=""):
		self.name = name
		if os.path.exists(path):
			self.path = path
		else:
			self.path = os.getcwd()
		self.filePath = '{}/{}'.format(self.path,self.name)
	
	def addRow(self,row):
		entry = row + '\n'
		self.file = open(self.filePath, 'a')
		self.file.write(entry)
		self.file.close()
		return entry
		
	def readCSVFile(self):
		self.file = open(self.filePath, 'r')
		contents = self.file.read()
		self.file.close()
		return contents
	
	def lineCount(self):
		try:
			self.file = open(self.filePath, 'r')
			lines = sum(1 for line in self.file)
			self.file.close()
		except IOError:
			lines = 0
		return lines
	
	def changeFileName(self,name,path=""):
		currentName = self.filePath
		if len(path) > 0 and os.path.exists(path):
			fullName = path + name
		else:
			fullName = self.path + name
		print name
		self.file.close()
		try:
			os.rename(currentName,fullName)
			self.name = name
			self.filePath = fullName
		except OSError:
			print 'A file with the name ' + str(name) + ' already exists'
		except:
			print "Unknown Error!!! Unable to rename file."

class xCSV():
    def __init__ (self, name, path="", dialect='excel', delimiter=',',quotechar='|'):
        if '.csv' not in name: # Check for .csv file extension
            name = name + '.csv'
        self.name = name
        self.dialect = dialect
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.data = [[]]
        if os.path.exists(path): 
            self.path = path
        else:
            if path != "":
                print "Unable to find specified path. Defaulting to current working directory."
            self.path = os.getcwd()
        self.filePath = self.path + '\\' + self.name
        
    def readFile (self):
        status = 0
        try:
            csvFile = open(self.filePath, 'r')
            status = 1
            try:
                import csv
                data = csv.reader(csvFile,self.dialect)
                for row in data:
                    self.data.append(row)
                status = 2
            except:
                pass
        except:
            status = 99
        csvFile.close()
        return data

    def readLines (self):
        pass

    def addRow(self,row=[]):
        status = 0
        try:
            csvFile = open(self.name, 'wb')
            status = 1
            try:
                import csv
                '''data = self.readFile()
                data.append(row)
                print data'''
                writer = csv.writer(csvFile,delimiter=self.delimiter)
                status = 2
                writer.write(row)
                '''
                try:
                    for row in data:
                        writer.writerows(row)
                    status = 3
                except:
                    pass'''
            except:
                pass
        except:
            status = 99
        csvFile.close()
        return status

def deleteAll(directory):
	for file in listdir(directory):
		filePath = path.join(directory, file)
		try:
			unlink(filePath)
		except Exception as e:
			print e
