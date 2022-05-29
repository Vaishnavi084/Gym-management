member_details={}
reg_dict={}
def_reg={18.5:{'Mon':'Chest','Tue':'Biceps','Wed':'Rest','Thu':'Back','Fri':'Triceps','Sat':'Rest','Sun':'Rest'},
        25.0:{'Mon':'Chest','Tue':'Biceps','Wed':'Cardio/Abs','Thu':'Back','Fri':'Triceps','Sat':'Legs','Sun':'Rest'},
        30.0:{'Mon':'Chest','Tue':'Biceps','Wed':'Abs/Cardio','Thu':'Back','Fri':'Triceps','Sat':'Legs','Sun':'Cardio'},
        31.0:{'Mon':'Chest','Tue':'Biceps','Wed':'Cardio','Thu':'Back','Fri':'Triceps','Sat':'Cardio','Sun':'Cardio'}}
class Gym():
    
    def __init__(self):
        print("Welcome To Fortitude Fitness Gym ")
        print(" ")
        print("PROFILE Menu")
        print('\n1.Super-User\n2.MEMBER\n0.Exit')
        inp=int(input('Enter Your Response: '))
        if inp==1:
            self.super_usermenu()
        elif inp==2:
            self.member_menu()
        elif inp==0:
            print('You have logged out of the system ')
    
    def super_usermenu(self):
            print('\nWelcome to super_user Interface')
            print('\nDisplaying Options')
            key=True
            while key:
                print('\n1.Create Member\n2.ViewMember\n3.DeleteMember\n4.UpdateMember\n5.CreateRegimen\n6.ViewRegimen\n7.DeleteRegimen\n8.UpdateRegimen\n0.Exit')
                inpu1=int(input('Please Choose an option: '))
                if inpu1==1:
                    self.create_mem()
                elif inpu1==2:
                    self.view_mem()
                elif inpu1==3:
                    self.del_mem()
                elif inpu1==4:
                    self.update_mem()
                elif inpu1==5:
                    self.create_regimen()
                elif inpu1==6:
                    self.view_regimen()
                elif inpu1==7:
                    self.del_regimen()
                elif inpu1==8:
                    self.update_regimen()
                elif inpu1==0:
                    key=False
                    print('You have exited the super_user portal')
                    self.__init__()
        
    def create_mem(self):
            print('\nWelcome to registration Portal')
            n=int(input('\nEnter the number of new users you need to add: '))
            for i in range(n):
                keys=member_details.keys()
                point=True
                while point:
                    self.name=input('Enter the full name: ')
                    self.Age=int(input('Enter your age: '))
                    if self.Age <18:
                        print("Sorry you can't join the gym")
                        break
                    self.Gender=input('Are You Male\Female\other ?: ')
                    while self.Gender not in  ['Male','Female','M','F','Other']:
                        print('\nPlease enter a valid gender')
                        self.Gender=input('Are You Male\Female\other ?: ')
                    self.Mob_num=int(input('Enter your Valid contact number: '))
                    if keys:
                        if self.Mob_num in keys:
                            print('\nThis contact exit already')
                            break
                    self.email=input('Enter your emailId: ')
                    self.weight=float(input('Enter your weight in kgs: '))
                    self.height=float(input('Enter your height in m: '))
                    self.Bmi=self.bmi(self.weight,self.height)
                    print('\nYour BMI is: ',self.Bmi)
                    if self.Bmi <18.5:
                        reg_dict[self.Mob_num]=def_reg[18.5]
                    elif self.Bmi <25.0 and self.Bmi >=18.5 :
                        reg_dict[self.Mob_num]=def_reg[25.0]
                    elif self.Bmi <30.0 and self.Bmi >=25.0:
                        reg_dict[self.Mob_num]=def_reg[30.0]
                    elif self.Bmi>=30.0:
                        reg_dict[self.Mob_num]=def_reg[31.0]
                    self.mem_dur=int(input('MemberShip you would like to select (1,3,6,12) months: '))
                    if self.mem_dur not in [1,3,6,12]:
                        print('Sorry! We dont provide the membership you selected')
                        break
                    member_details[self.Mob_num]=[self.name,self.Age,self.Gender,self.Mob_num,self.email,self.Bmi,self.mem_dur]
                    print('\nYou have been successfully registered as a member ')
                    point=False

        
    def view_mem(self):
            print('\nMEMBER DETAILS\n')
            keys=member_details.keys()
            if keys:
                for i in keys:
                    print('Full Name: ',member_details[i][0])
                    print('Age: ',member_details[i][1])
                    print('Gender: ',member_details[i][2])
                    print('Contact Number: ',member_details[i][3])
                    print('Email ID: ',member_details[i][4])
                    print('BMI: ',member_details[i][5])
                    print('Membership Duration: ',member_details[i][6])
                    print('\n--------------------------------------------\n')
            else:
                print('\nNo members have joined our Gym')
    
    def disp_mem(self):
        num=int(input('\nEnter the contact number: '))
        keys=member_details.keys()
        if num in keys:
            print('\nFull Name: ',member_details[num][0])
            print('Age: ',member_details[num][1])
            print('Gender: ',member_details[num][2])
            print('Contact Number: ',member_details[num][3])
            print('Email ID: ',member_details[num][4])
            print('BMI: ',member_details[num][5])
            print('Membership Duration: ',member_details[num][6])
        elif num not in keys:
            print("Sorry!! It seems you haven't been registered as a member.Contact super_user for registration")
    
    def del_mem(self):
        print('\nDeleting Member details')
        keys=member_details.keys()
        if keys:
            for i in keys:
                print(i,member_details[i][0])
            num=int(input('\nEnter the contact number: '))
            print('Member: ',member_details[num][0])
            resp=input('\nAre you sure You want to delete this member  Y/N ?: ')
            if resp=='Y':
                member_details.pop(num)
                reg_dict.pop(num)
                print('\nMember deleted')
            elif resp=='N':
                print('\nContinue the service of our Gym')
        else:
            print('\nNo members in Gym')
    
    def update_mem(self):
        print('\nMember Updation Portal')
        keys=member_details.keys()
        if keys:
            for i in keys:
                print(i, member_details[i][0])
            no=int(input('\nEnter the contact number: '))
            if no in keys:
                print('\nChoose the option you want to update')
                flag=True
                while flag:
                    respo=int(input('\n1.FullName\n2.Age\n3.Gender\n4.EmailId\n5.BMI\n6.Extend Membership Duration\n7.Revoke Membership\n0.Exit\nEnter your choice: '))
                    if respo==1:
                        member_details[no][0]=input('Full Name: ')
                    if respo==2:
                        member_details[no][1]=input('Age: ')
                    if respo==3:
                        member_details[no][2]=input('Gender: ')
                    if respo==4:
                        member_details[no][4]=input('Email ID: ')
                    if respo==5:
                        member_details[no][5]=input('BMI: ',)
                    if respo==6:
                        member_details[no][6]=input('Membership Duration: ')
                    if respo==7:
                        print('Do you want to revoke the {0} membership ?'.format(member_details[no][0]))
                        rep=input('Enter Y/N: ')
                        if rep=='Y':
                            member_details.pop(no)
                            reg_dict.pop(no)
                            print('\nYour membership is cancelled successfully')
                            break
                        elif rep=='N':
                            print('You can try updating other details')
                    if respo==0:
                        flag=False
        else:
            print('\nNo members in Gym')
    
    def create_regimen(self):
        print('\nRegime Creation Portal')
        key=member_details.keys()
        if key:
            for i in key:
                print(i, member_details[i][0])
            cont=int(input('\nEnter the contact number: '))
            if cont in key:
                print('\nCreating new regime for {0} with BMI {1}'.format(member_details[cont][0],str(member_details[cont][5])))
                if (member_details[cont][5]) <18.5:
                        reg_dict[cont]=def_reg[18.5]
                elif (member_details[cont][5])<25.0 and (member_details[cont][5]) >=18.5 :
                    reg_dict[cont]=def_reg[25.0]
                elif (member_details[cont][5])<30.0 and (member_details[cont][5])>=25.0:
                    reg_dict[cont]=def_reg[30.0]
                elif (member_details[cont][5])>=30.0:
                    reg_dict[cont]=def_reg[31.0]
                print('\nWorkout regime created')
        else:
            print('\nNo members joined')
    
    def view_regimen(self):
        print('\nWORKOUT SCHEDULE FOR ALL MEMBERS')
        key=reg_dict.keys()
        if key:
            for i in key:
                print('\nMember Name: ',member_details[i][0])
                print('Monday: ',reg_dict[i]['Mon'])
                print('Tuesday: ',reg_dict[i]['Tue'])
                print('Wednesday: ',reg_dict[i]['Wed'])
                print('Thursday: ',reg_dict[i]['Thu'])
                print('Friday: ',reg_dict[i]['Fri'])
                print('Saturday: ',reg_dict[i]['Sat'])
                print('Sunday: ',reg_dict[i]['Sun'])
                print('\n--------------------------------------\n')
        else:
            print('Sorry!! No workout schedule in gym')
            
    def del_regimen(self):
        print('\nDeletion Portal')
        key=reg_dict.keys()
        if key:
            for i in key:
                print(i,member_details[i][0])
            con=int(input('Enter the contact number: '))
            if con in key:
                print('Do you want to delete the workout regime of {}'.format(member_details[con][0]))
                resp=input('Enter your response:Y/N?: ')
                if resp=='Y':
                    reg_dict.pop(con)
                    print('\nWorkout regime deleted!!')
                elif resp=='N':
                    print('\nContinue your work schedule')
            else:
                print('Sorry!! No workout schedule in gym')
        else:
            print('\nNo members have joined our gym')
    
    def update_regimen(self):
        print('\nUpdation Portal')
        key=reg_dict.keys()
        for i in key:
            print(i,member_details[i][0])
        if key:
            con=int(input('Enter the contact number: '))
            if con in key:
                print('Choose the Day you want to update')
                flags=True
                while flags:
                    resp=int(input('\n1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday\n0.Exit\nEnter your response: '))
                    if resp==1:
                        reg_dict[con]['Mon']=input('Monday: ')
                    if resp==2:
                        reg_dict[con]['Tue']=input('Tuesday: ')
                    if resp==3:
                        reg_dict[con]['Wed']=input('Wednesday: ')
                    if resp==4:
                        reg_dict[con]['Thu']=input('Thursday: ')
                    if resp==5:
                        reg_dict[con]['Fri']=input('Friday: ')
                    if resp==6:
                        reg_dict[con]['Sat']=input('Saturday: ')
                    if resp==7:
                        reg_dict[con]['Sun']=input('Sunday: ')
                    if resp==0:
                        flags=False
            else:
                print('\nThis member has no workout regime')
        else:
            print('\nNo workout regime has been started')
#######################################################################################################################    
    def member_menu(self):
        print('\nWelcome to Member Portal')
        print('\nDisplaying Options')
        tick=True
        while tick:
            inpu2=int(input('\n1.My Regime\n2.My Profile\n0.Exit\nEnter your response: '))
            if inpu2==1:
                self.view_regime()
            if inpu2==2:
                self.profile()
            if inpu2==0:
                tick=False
                print('\nYou have exited member portal')
                self.__init__()
             
    def view_regime(self):
        print('\nWorkout Regime')
        key=reg_dict.keys()
        if key:
            cont=int(input('\nEnter your contact number:'))
            if cont in key:
                print('\nMonday: ',reg_dict[cont]['Mon'])
                print('Tuesday: ',reg_dict[cont]['Tue'])
                print('Wednesday: ',reg_dict[cont]['Wed'])
                print('Thursday: ',reg_dict[cont]['Thu'])
                print('Friday: ',reg_dict[cont]['Fri'])
                print('Saturday: ',reg_dict[cont]['Sat'])
                print('Sunday: ',reg_dict[cont]['Sun'])
            else:
                print('\nYou havent started a workout regime yet!!')
        else:
            print('\nPlease Contact super_user!!')

    def profile(self):
        key=member_details.keys()
        if key:
            cont=int(input('\nEnter your contact number: '))
            if cont in key:
                print('\nFull Name: ',member_details[cont][0])
                print('Age: ',member_details[cont][1])
                print('Gender: ',member_details[cont][2])
                print('Contact Number: ',member_details[cont][3])
                print('Email ID: ',member_details[cont][4])
                print('BMI: ',member_details[cont][5])
                print('Membership Duration: ',member_details[cont][6])
            else:
                print('\nYou arent a member in the gym.Contact super_user for attaining a memberhip!!')
        
    @staticmethod
    def bmi(weight,height):
        bmi_cal=weight/(height**2)
        return bmi_cal
            
obj=Gym()       
    
    

                
                
                
          
        
        
        
            
                
                             
                    
            
