import psycopg2
params_dic = {
  "port":"5432",
  "dbname":"statscan",
  "user":"postgres",
  "password":"PoBuCe60"
}

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE sunshine
        (
          id bigint,
          sector VARCHAR(56),
          last_name VARCHAR(26),
          first_name VARCHAR(25),
          salary decimal(12,2),
          taxable decimal(11,2),
          employer VARCHAR(193),
          job_title VARCHAR(300),
          calendar_year bigint
        );
        """)
    conn = None
    try:
        # read the connection parameters
        #params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params_dic)
        cur = conn.cursor()
        # create table
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()

    conn = psycopg2.connect(**params_dic)
    cur = conn.cursor()

    with open('data/2019.csv', 'r') as file:
        next(file) # Skip the header row.
        cur.copy_from(file, table='sunshine', sep='|')
        #Commit Changes and close connection
        conn.commit()
        conn.close()

    """
    csv_file = open(r'data/2019_second.csv', 'r')
    cur.copy_from(csv_file, table='sunshine', sep='|')
    csv_file.close()
    conn.commit()

    cur.close()
    conn.close()
    """
