from datetime import datetime,date  #python library which contains date and tine methods
import os                           #python library which contains file and folder searching methods


class Employee:

    def Name(self,name,lastname,pay,opis):
        
        self.name = name
        self.lastname = lastname
        self.pay = pay
        self.opis = opis
        self.email = name + "." + lastname + "@gmail.com" # ovdje je greška što sam izbrisao bio + "@gmail.com"
     
    def CheckAllEmails(self,filename, list_emails,count):
        file = open(filename, "r")
        read = file.readlines()
        file.close()
        self.count = 0
        for word in list_emails:
            lower = word.lower()
            
            for sentence in read:
                line = sentence.split()
                for each in line:
                    line2 = each.lower()
                    line2 = ''.join([i for i in line2 if not i.isdigit()]) #remove numbers from the name.lastname1 examle -> name.lastname to compare same name.lastname in files
                    if lower == line2:  
                        count += 1
                        self.count = count
            
            print(lower,":",count)        
      
i=0
while 1:
    i += 1
    Date = str(date.today())
    filename = 'Employee_'+Date+'.txt'
    saveFile = open(filename,'a') # 'a' - append (adding more text to same text file), 'w' - write (write new text to text file(deleting the preveous)), 'r' -read (reading text file)
    print(i,". employee")
    name1= input("Ime: ")
    lastname1 = input("Prezime: ")
    pay1 = int(input("Plaća: ")) 
    opis = input("Opis: ")
    
    if name1 == 'q'or name1 == 'quit' or lastname1 == 'q' or lastname1 == 'quit' or pay1 == 0 : break
    
    employee1 = Employee()
    employee1.Name(name1,lastname1,pay1,opis)
    employee2 = Employee()
    
    path = 'C:\\users\user_name\Desktop\Python'  #<-------- PUT YOUR DIRECTORY PATH HERE
    x = os.listdir(path)
    for file in x:
        if file.startswith("Employee") and file.endswith(".txt"): # startswith() is method which recognize all string or files start with the same starting name, and endswith() is method which recognize the end of string or file name with the same ending name (word or letter)
           z = os.path.join(path,file)
    zz = "Employee_2019-04-04.txt"
    employee2.CheckAllEmails(zz, [employee1.email],0) 
    
    if employee2.count > 0:             
        addNum = str(employee2.count)  
        Email = employee1.name + "." + employee1.lastname + addNum +"@gmail.com"
    else:  
        Email = employee1.name + "." + employee1.lastname + "@gmail.com"
        

    saveFile.write("\n"+employee1.name + "\n"+ employee1.lastname+"\nemail: "+ Email + "\nplaća u eurima: "+"\n"+'%d' % pay1+"\n"+opis+"\n")
    x = str(datetime.now())
    xx = x+"\n"
    saveFile.write(xx)
    saveFile.close()
    
    print(employee1.name + " "+ employee1.lastname+" email: "+ Email + " plaća u eurima: "+'%d' %pay1 +"\n")
    print(z)
    
    
    




   
