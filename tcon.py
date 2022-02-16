'''  1.Install cx_oracle
      on windows the command is python -m pip install cx_Oracle --upgrade
      on Linux/mac python3 -m pip install cx_Oracle --upgrade
      2.install the oracle instant client basic and add its path to your PATH  variable '''
import cx_Oracle
import sys
import config
lib_dir = r"C:\instantclient_19_13"

try:
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
except Exception as err:
    print("Error connecting: cx_Oracle.init_oracle_client()")
    print(err);
    sys.exit(1);

try:
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as con:
                  print(con.version)
                  cur = con.cursor()
                  cur.execute('Select * from hr.employees')
                  result=cur.fetchmany(numRows=3)
                  print (result )
                  ''' 
                  for result in cur:
                          print ( result )
                  '''
                  cur.close()
                  con.close()
except cx_Oracle.Error as error:
	    print(error)

