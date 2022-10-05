DB=mysql.connnector.connect(**config) 

Print(“\n  Database user {} connected to MYSQL on host {} with database {} ”.format((config[“user”], Config[“host”], Config [“database”])) 

Input(“\n\n press any to continue . . .”) 

 

Except mysql.connector.Error as err: 

If err.errno == errorcode.ER_ACCESS_denied_ERROR: 

        Print(* The supplied username or password are inavlid”) 

Eliff err.errno == errorcode.er_bad_DB_ERROR 

       Print(* The specified database does not exist*) 

      else: 

             Print(err) 

        FInally: 

           Db.close{}  


 
