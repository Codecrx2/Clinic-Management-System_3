import pandas as pd
login=pd.read_csv('prescription.csv')
l2=pd.read_csv('Patients_main.csv')
acsv=pd.read_csv("admin.csv")
aname=input("Enter your Name-->")
apass=input("Enter your Password-->")
aif=acsv.loc[(acsv.Name==aname)]
aif2=acsv.loc[(acsv.Password==apass)]
adminn='Manish'
adminp='ms'








def system():
      while True:
            print('''             ***************************************
                    Clinic Management System
             ***************************************
             *************M̳A̳I̳N̳ M̳E̳N̳U̳*****************
               1. Old Records
               2. New Patient(New Record)
               3. Exit System
             ***************************************''')
            choice=int(input("Enter the function-->"))
            print(l2)
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
                    
            elif choice==2:
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
            elif choice==3:
                  break
            else:
                  print("Incorrect Input")
                  print("Try Again.")









'''
while True:
      if aif.empty:
            print("Failed")
      else:
            print('Logged In')
            if aif2.empty:
                  print("Failed")
                  c=input("Are you a new Employee(Y/N)-->")
                  if c.upper()=='Y':
                        anamem=input("Enter Administrator Name")
                        apassm=input("Enter Administrator Password")
                        if anamem==adminn:
                              newname=input("Name-->")
                              newpass=input("Password-->")
                              newpass1=input("Password(Confirmation)-->")
                              if newpass==newpass1:
                                    system()
                              else:
                                    print("Try Again")
                        else:
                              print("Try Again")
                  else:
                        print("Try Again")
            else:
                  print("Failed")
                  
          while True:
               print('             ***************************************
                    Clinic Management System
             ***************************************
             *************M̳A̳I̳N̳ M̳E̳N̳U̳*****************
               1. Old Records
               2. New Patient(New Record)
               3. Exit System
             ***************************************')
               choice=int(input("Enter the function-->"))
               print(l2)
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
                    
               elif choice==2:
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
               elif choice==3:
                    break
               else:
                    print("Incorrect Input")
                    print("Try Again.")
                  '''
print('Clinic Management System Ended')
