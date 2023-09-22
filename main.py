import pandas as pd
import defined
login=pd.read_csv('prescription.csv')
l2=pd.read_csv('Patients_main.csv')
acsv=pd.read_csv("admin.csv")
app=pd.read_csv("Appointment.csv")
aname=input("Enter your Name-->")
apass=input("Enter your Password-->")
adminn='Manish'
adminp='nms'
aif=acsv.loc[(acsv.Name==aname)]
aif2=acsv.loc[(acsv.Password==apass)]










#Defining a Function called system
#We have defined this Function so it is easier
#for use to find the error in the code
#We will use this Function later in the code
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
                    print("""             ***************************************
                    Clinic Management System
             ***************************************
             *************C̳U̳S̳T̳O̳M̳E̳R̳ R̳E̳C̳O̳R̳D̳S̳*****************
               1. Previous Records
               2. Old Medicines Given
               3. Exit System
             ***************************************""")
                    choice2=input(">>>")
                    if choice2==1:
                         pid2=int(input("Enter Patient ID"))
                         if pid2==login.Patient_ID:
                              print('Here:-')
                         else:
                              print("Incorrect Patient ID Entered")
                    elif choice2==3:
                         break
                    break
                    
          elif choice==2:
               print('-------------------New Patient-------------------')
               print("Enter your First Name")
               userfname=input(">>>")
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
               break
          elif choice==3:
               break
          else:
               print("Incorrect Input")
               print("Try Again.")









#Checking If The Employee Name Matches A Name In The Clinic DataBase
if aif.empty:
     print("Failed")
else:
     #Checking If The Employee Password Matches The
     #Password In Front Of The Previously Entered Name
     if aif2.empty:
          print("Failed")
          c=input("Are you a new Employee(Y/N)-->")
          if c.upper()=='Y':
               anamem=input("Enter Administrator Name")
               apassm=input("Enter Administrator Password")
               if anamem==adminn:
                    if apassm==adminp:
                         newname=input("Name-->")
                         newpass=input("Password-->")
                         newpass1=input("Password(Confirmation)-->")
                         if newpass==newpass1:
                              list12=[newname,newpass]
                              print(list12)
                              acsv.loc[len(acsv.index)] = list12
                              acsv.to_csv('admin.csv',index=False)
                         else:
                              print("The Passwords Do Not Match")
                    else:
                         print("Incorrect Admin Password")
               else:
                    print("Incorrect Admin Name")
          else:
               print("If You Are Not A New Employee")
     else:
          system()

print('Clinic Management System Ended')
