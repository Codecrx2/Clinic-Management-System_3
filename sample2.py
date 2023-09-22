import pandas as pd
import defined
login=pd.read_csv('prescription.csv')
l2=pd.read_csv('Patients_main.csv')
acsv=pd.read_csv("admin.csv")
aname=input("Enter your Name-->")
apass=input("Enter your Password-->")
aif=acsv.loc[(acsv.Name==aname)]
aif2=acsv.loc[(acsv.Password==apass)]
adminn='Manish'
adminp='ms'
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
                         ls1=[newname,newpass]
                         print(ls1)
                         acsv.loc[len(acsv.index)] = ls1
                         acsv.to_csv('admin.csv',index=False)
                         defined.system()
                    else:
                         print("Try Again")
               else:
                    print("Try Again")
          else:
               print("Try Again")
     else:
          defined.system()
print('Clinic Management System Ended')
