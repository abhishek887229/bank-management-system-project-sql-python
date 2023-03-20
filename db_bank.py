import mysql.connector
import datetime
import os

 
 

         
 #for formatting
def abhi():
    input('\nenter to continue......')
    os.system('clear')

def abhi_mini():
     os.system('clear')

def max4():
                z_pin=int(input('enter pin max 4 digit:-\t'))
                z_confirm_pin=int
                if z_pin>9999:
                    print('you enter value more then 4 digit please enter max length 4.')
                    return max4()
                elif z_pin<9999:
                    return z_pin
                
def create_account():
    print("-----------------------------------------\n")
    print("--------db bank Account Creation---------\n")
    print("-----------------------------------------\n")
    #user Input
    user_name=input('enter your name -->\t')
    print('\n')
    initial_balance=input('enter your initial balance -->\t')
    print('\n')
    user_pin=max4()
    #self generated id
    
    x = datetime.datetime.now()

    z=(x.strftime("%S"))
    z1=(x.strftime("%M"))
    z2=(x.strftime("%H"))
    z3=(x.strftime("%d"))
    #our unique id
    unique=z+z1+z2+z3
    abhi()

    try:
        register_db=mysql.connector.connect(
            host='localhost',
            user="root",
            password="",
            database="db_bank"
            )
        #creating cursor for cur
        cur=register_db.cursor()
        #command for create account
        insert_Data="""insert into reg(unique_id,name,inital_balance,pin)
                    values(%s,%s,%s,%s);
                     """
        #value
        insert_value=(unique,user_name,initial_balance,user_pin)
        #execute the code
        cur.execute(insert_Data,insert_value)
        register_db.commit()
        
        print("\n\n")
        print("--------------------------------------------------\n")

        print('your unique id is :- {} '.format(unique))

        print("\nplease remember your unique id to do the transaction in future.")
        abhi()
    except mysql.connector.Error as e:
        print(e)
        abhi()
        create_account()


def dr_money_from_account():
     
     abhi_mini()
     # get value from data base for checking :-
     #extract values 
     #  1)unique id
     #  2) name
     #  3) pin
     #  4) initial_balance
     print("-----------------------------------------\n")
     print("--------db bank money withdrawal-------------\n")
     print("-----------------------------------------\n")
     id_user=(input('enter your unique id -->\t'))
     id_user2=int(id_user)

     try:
          register_db=mysql.connector.connect(
            host='localhost',
            user="root",
            password="",
            database="db_bank"
            )
          debit_curosr=register_db.cursor()
          command="""
          select * from reg 
          where unique_id=%s;
          """
          debit_curosr.execute(command,(id_user,))
          data_from_db=debit_curosr.fetchall()
          #data which extract from database
          unique_id=[a[1] for a in data_from_db]
          name=[a[2] for a in data_from_db][0]
          balance=[a[3] for a in data_from_db][0]
          pin=[a[4] for a in data_from_db][0]
          if id_user2 in unique_id:
               abhi_mini()
               print('-------------------------------------------------------\n\n')
               print('welcome Mr./Mrs. {}\t\t{}'.format(name,datetime.datetime.now()))
               print('-------------------------------------------------------\n\n')

               debit_amount=input('enter amount you want to widthDraw -->\t')
               db2=int(debit_amount)
               print('\n')
               if db2>balance:
                    print("not enought balance")
                    abhi()
                    main()
               else:
                    debit_pin=input('enter your pin -->\t')
                    print("\n")
                    debit_pin_int=int(debit_pin)
                    if debit_pin_int==pin:
                                
                            #connect to database
                                try:
                                    register_db=mysql.connector.connect(
                                    host='localhost',
                                    user="root",
                                    password="",
                                    database="db_bank"
                                    )

                                    insert_data_debit="""insert into 
                                                        debit(unique_id,inital_balance,debit_money)
                                                        values(%s,%s,%s);
                                                    """
                                    insert_data_transaction="""insert into 
                                                        transaction(unique_id,initial_balance,debit)
                                                        values(%s,%s,%s);
                                                    """
                                    #value insertion
                                    insert_value_debit=(id_user,balance,debit_amount)
                                    insert_value_debit1=(id_user,balance,debit_amount)
                                    #cursor for insert data
                                    data_insert=register_db.cursor()
                                    data_insert1=register_db.cursor()
                                    #execute table
                                    data_insert.execute(insert_data_debit,insert_value_debit)
                                    data_insert1.execute(insert_data_transaction,insert_value_debit1)
                                    #commit chnage in db
                                    register_db.commit()

                                    #update table 
                                    update_data="""update reg set inital_balance=inital_balance-%s
                                                    where unique_id=%s;
                                                """
                                    
                                    update_balance="""update transaction set balance=%s-%s
                                                    where unique_id=%s;
                                                """
                                    #valuue insertion
                                    update_val=(debit_amount,id_user)

                                    update_user_balance=(balance,debit_amount,id_user)
                                    #curssor creating
                                    data_update_for_db=register_db.cursor()
                                    bal_update_for_db=register_db.cursor()
                                    #execute 
                                    data_update_for_db.execute(update_data,update_val)
                                    bal_update_for_db.execute(update_balance,update_user_balance)
                                    #commit chnage
                                    register_db.commit()
                                    

                                except mysql.connector.Error as e:
                                    print(e)
                                    abhi()
                                    create_account()
                                
                    
                                print('your your transaction done\n\n')
                                print('thank you :)\n')
                                abhi()

                    else:
                            print('you enter wrong pin')
                            dr_money_from_account()
                    
          else:
               print('error ')
               create_account()




     except mysql.connector.Error as e:
        print(e)
        abhi()
        create_account()
#--------------------------------------------------------------------------------------------------
#fuction for credit of money....
#--------------------------------------------------------------------------------------------------
def deposit_money_to_account():
     
     abhi_mini()
     # get value from data base for checking :-
     #extract values 
     #  1)unique id
     #  2) name
     #  3) pin
     #  4) initial_balance
     abhi_mini()
     print("-----------------------------------------\n")
     print("--------db bank money deposit-------------\n")
     print("-----------------------------------------\n")
     id_user=(input('enter your unique id to start transaction -->\t'))
     id_user2=int(id_user)

     try:
          register_db=mysql.connector.connect(
            host='localhost',
            user="root",
            password="",
            database="db_bank"
            )
          credit_curosr=register_db.cursor()
          command="""
          select * from reg 
          where unique_id=%s;
          """
          credit_curosr.execute(command,(id_user,))
          data_from_db=credit_curosr.fetchall()
          #data which extract from database
          unique_id=[a[1] for a in data_from_db]
          name=[a[2] for a in data_from_db][0]
          balance=[a[3] for a in data_from_db][0]
          pin=[a[4] for a in data_from_db][0]
          if id_user2 in unique_id:
               abhi_mini()
               print('-------------------------------------------------------\n\n')
               print('welcome Mr./Mrs. {}\t\t{}'.format(name,datetime.datetime.now()))
               print('-------------------------------------------------------\n\n')

               credit_amount=input('enter amount you want to Deposite into your account -->\t')
               print('\n')
               credit_pin=input('enter your secret pin --->\t')
               print('\n')
               credit_pin_int=int(credit_pin)
               abhi()
               if credit_pin_int==pin:
                        #ERROR FCHECK FOR GETMONEY FCUTION
                        #A INTERNAL EXCEPTION HANDLER
                        try:
                            register_db=mysql.connector.connect(
                            host='localhost',
                            user="root",
                            password="",
                            database="db_bank"
                            )
                            #credit table contain 
                            # 1)cr_id 
                            # 2)unique_id 
                            # 3)initial_balance 
                            # 4)credit_money 
                            # 5)datetime of transaction


                            insert_data_debit="""insert into credit(unique_id,initial_balance,credit_money)
                                            values(%s,%s,%s);"""
                            
                            insert_data_transaction="""insert into 
                                                 transaction(unique_id,initial_balance,credit)
                                                 values(%s,%s,%s);
                                              """
                            
                            
                            insert_value_credit=(id_user,balance,credit_amount)
                            insert_value_transaction=(id_user,balance,credit_amount)

                            data_insert=register_db.cursor()
                            data_insert1=register_db.cursor()


                            data_insert.execute(insert_data_debit,insert_value_credit)
                            data_insert1.execute(insert_data_transaction,insert_value_transaction)
                            register_db.commit()
                        
                            
                            update_data="""update reg set inital_balance=inital_balance+%s
                                            where unique_id=%s;
                                        """
                            
                            update_balance="""update transaction set balance=%s+%s
                                            where unique_id=%s;
                                        """
                            


                            update_val=(credit_amount,id_user)
                            update_user_balance=(balance,credit_amount,id_user)

                            data_update_for_db=register_db.cursor()
                            bal_update_for_db=register_db.cursor()
                            data_update_for_db.execute(update_data,update_val)
                            bal_update_for_db.execute(update_balance,update_user_balance)
                            
                            register_db.commit()


                        except mysql.connector.Error as e:
                            print(e)
                            abhi()
                            deposit_money_to_account()

               
                        print('your your transaction done')
                        print("thank you :)")
                        abhi()
               else:
                    print('you enter wrong pin')
                    abhi()
                    main()
                    
          else:
               print('error in transaction')
               deposit_money_to_account()



     except mysql.connector.Error as e:
        print(e)
        abhi()
        create_account()



def balance():
    print("-----------------------------------------\n")
    print("--------db bank balance Check-------------\n")
    print("-----------------------------------------\n\n")

    id_user=(input('enter your unique id to start transaction -->\t'))
    id_user2=int(id_user)
    try:
          register_db=mysql.connector.connect(
            host='localhost',
            user="root",
            password="",
            database="db_bank"
            )
          #cursor crreating
          credit_curosr=register_db.cursor()
          #Sql command
          command="""
          select inital_balance,name from reg 
          where unique_id=%s;
          """
          #execution of command
          credit_curosr.execute(command,(id_user,))
          #extraction of data from db and store in data_from_db
          data_from_db=credit_curosr.fetchall()
          data=[a[0] for a in data_from_db]
          name=[a[1] for a in data_from_db]
          print("----------------------------------------------------------------------------\n\n")
          print("name:- {}\n".format(name[0]))
          print("your account balance is "+'"{}"'+" at time {}".format(data[0],datetime.datetime.now()))
          print("-----------------------------------------------------------------------------\n\n")
          abhi()
          main()

    except mysql.connector.Error as e:
        print(e)
        abhi()
        create_account()
#--------------------
#---------transaction
#--------------------
def transaction():
    print("-----------------------------------------\n")
    print("--------db bank transaction history------\n")
    print("-----------------------------------------\n\n")
    unique_id=input('enter unique id -->')

    print("\n")
    try:
          register_db=mysql.connector.connect(
            host='localhost',
            user="root",
            password="",
            database="db_bank"
            )
          #cursor crreating
          credit_curosr=register_db.cursor()
          #Sql command
          command="""
          select * from transaction  
          where unique_id=%s ;
          """
          #execution of command
          credit_curosr.execute(command,(unique_id,))
          #extraction of data from db and store in data_from_db
          data_from_db=credit_curosr.fetchall()
          print("no ||   date               unique_id      inittal_bal       debit            credit ")
          for i in data_from_db:
                print(str(i[0])+"  ||"+str(i[1])+"  || "+str(i[2])+"    ||  "+str(i[3])+"   ||               "+str(i[4])+"   ||      "+str(i[5])+"   ||  ")
          print("----------------------------------------------------------------------------------------")
          print("your balance till now:-{}".format(str(data_from_db[0][6])))      
          print("----------------------------------------------------------------------------------------\n\n")
          abhi()
          

    except mysql.connector.Error as e:
        print(e)
        abhi()
        create_account()
    
    abhi_mini()
     
     

def main():
    print("************************************************************")
    print("========== WELCOME TO ITSOURCECODE BANKING SYSTEM ==========")
    print("************************************************************\n\n")
    print("========== (a). Open New Client Account    | (b). The Client Withdraw a Money")
    print("========== (c). The Client Deposit a Money | (d). Check Clients & Balance")
    print("========== (e). See transaction            | (x). Quit \n\n")
    print("************************************************************")

    Letter = str(input("Select a Letter from the Above Box menu --> ")).lower()

    if Letter=='a':
        # Clearing the Screen
        os.system('clear')
        create_account()
        main()
    elif Letter=='b':
        # Clearing the Screen
        os.system('clear')
        dr_money_from_account()
        main()
    elif Letter=='c':
        # Clearing the Screen
        os.system('clear')
        deposit_money_to_account()
        main()
    elif Letter=='d':
        # Clearing the Screen
        os.system('clear')
        balance()
        main()
    elif Letter=='e':
        # Clearing the Screen
        os.system('clear')
        transaction()
        main()

    elif Letter=='x':
        # Clearing the Screen
        os.system('clear')
        exit()
    else:
        main()




main()
os.system('clear')







