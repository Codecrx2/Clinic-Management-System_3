import pandas as pd
import defined
import datetime
today=datetime.date.today();
login=pd.read_csv('prescription.csv')
l2=pd.read_csv('Patients_main.csv')
acsv=pd.read_csv("admin.csv")
app=pd.read_csv("Appointment.csv")
aname=input("Enter your Name-->")
apass=input("Enter your Password-->")
adminn='Manish'
adminp='nms'
#aif=acsv.loc[(acsv.Name==aname)]
aif3= acsv[(acsv["Name"] == aname) & (acsv["Password"] == apass)]
#aif2=acsv.loc[(acsv.Password==apass)]










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
               3. Appointment
               4. Exit System
             ***************************************""")
                    print("Enter you choice")
                    choice2=int(input(">>>"))
                    if choice2==1:
                        pid2=int(input("Enter Patient ID"))
                        df2=l2.loc[(pid2==l2.Patient_ID)]
                        if df2.empty:
                            print("Incorrect Patient ID Entered")
                        else:
                            print('Patients Old Records')
                            print(df2)
                    elif choice2==2:
                         pid2=int(input("Enter Patient ID"))
                         df2=login.loc[(pid2==login.Patient_ID)]
                         if df2.empty:
                              print("Incorrect Patient ID Entered")
                         else:
                              print("Medicines Given")
                              print(df2)
                    elif choice2==3:
                         pid2=int(input("Enter Patient ID"))
                         df2=login.loc[(pid2==login.Patient_ID)]
                         if df2.empty:
                              print("Incorrect Patient ID Entered")
                         else:
                              print('''             ***************************************
                    Clinic Management System
             ***************************************
             *************Appointments****************
               1. Book An Appointment
               2. Upcoming Appointment
               3. Cancel An Appointment
               4. Exit System
             ***************************************
             Enter The Number Of Function You Wish To Use''')
                              choice3=input(">>>")
                              if choice3==1:
                                   print(app)
                    elif choice2==4:
                         break
                    else:
                         break
                    break
                    
          elif choice==2:
               print('-------------------New Patient-------------------')
               print("Enter your First Name")
               userfname=input(">>>")
               userlname=input('Enter your Last Name-->')
               gender1=input("Enter your Gender(M/F)-->")
               userdob=input("Enter your Date of Birth(DD-MM-YYYY)-->")
               userall=input("Enter Your Allergies(Seperated with commas)-->")
               doc=input("Enter The Doctor's name")
               medname=input("Enter Medicine Name")
               medtime=input("Medicine Is Given For How Many Days")
               userfname2=userfname.lower()
               userlname2=userlname.lower()
               gender=gender1.upper()
               userall2=userall.upper()
               print("Congratulations")
               print("New Account Created")
               pid=len(l2.index)+1
               med=today+medtime
               doctype=login.loc[(login.Doctor_Name==doc)]['Doctor_type']
               ls1 = [pid,userfname2,userlname2,gender,userdob,userall2]
               print(ls1)
               l2.loc[len(l2.index)] = ls1
               l2.to_csv('Patients_main.csv',index=False)
               ls2=[pid,today,today,med,medname,doc,doctype]
               login.loc[len(login.index)]=ls2
               login.to_csv('Prescription.csv',index=False)
               break
          elif choice==3:
               break
          else:
               print("Incorrect Input")
               print("Try Again.")









#Checking If The Employee Name Matches A Name In The Clinic DataBase
if aif3.empty:
     print("Failed")
else:
     #Checking If The Employee Password Matches The
     #Password In Front Of The Previously Entered Name
     if aif3.empty:
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
