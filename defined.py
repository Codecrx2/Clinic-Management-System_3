import pandas as pd
login=pd.read_csv('prescription.csv')
l2=pd.read_csv('Patients_main.csv')

choice=0
def start():
      print('''             ***************************************
                    Clinic Management System
             ***************************************
             *************M̳A̳I̳N̳ M̳E̳N̳U̳*****************
               1. Old Records
               2. New Patient(New Record)
               3. Exit System
             ***************************************''')
      choice=int(input("Enter the function(Enter the Function Number)-->"))
      return choice                                                                                                                                                                                                                                                                                               #bewakoof


def check1():
      if choice==1:
            print('\t-------------------Login-------------------')
            log1=input('Enter your First Name-->')
            log2=input('Enter your Last Name-->')
            #df = login.loc[login.Password == passkey.lower()]
            df=l2.loc[(l2.Name==log1)]
            if df.empty:
                  print("Failed")
            else:
                  print('Welcome Mr.', log2)


def check2():
      
      print('-------------------New Patient-------------------')
      userfname=input("Enter your First Name-->")
      userlname=input('Enter your Last Name-->')
      gender1=input("Enter your Gender(M/F)-->")
      userdob=input("Enter your Date of Birth(DD-MM-YYYY)-->")
      userall=input("Enter your Allergies(Seperated with commas)-->")
      userfname2=userfname.lower()
      userlname2=userlname.lower()
      gender=gender1.upper()
      userall2=userall.upper()
      print("Congratulations")
      print("New Account Created")
      pid=len(l2.index)+1
      ls = [pid,userfname2,userlname2,gender,userdob,userall2]
      print(ls)
      l2.loc[len(l2.index)] = ls
      l2.to_csv('Patients_main.csv',index=False)


def check4():
      print("Incorrect Input")
      print("Try Again.")

def system():
      while True:
            if choice==1:
                  check1()
            elif choice==2:
                  check2()
            elif choice==3:
                  break
            else:
                  check4()


