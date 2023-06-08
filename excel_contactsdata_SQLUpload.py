import pandas as pd
import numpy as np
import mysql.connector
from mysql.connector import Error

file_path = r'C:\Users\New User\Segmentation\Data\DataCSV.xlsx'
data_df = pd.read_excel(file_path, sheet_name= 'contacts')

contacts_df = data_df.groupby('Company').agg({
    'Internal contact 1': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Role 1': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'External contact 1': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Internal contact 2': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Role 2': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'External contact 2': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Internal contact 3': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Role 3': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'External contact 3': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Internal contact 4': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Role 4': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'External contact 4': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Internal contact 5': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Role 5': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'External contact 5': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
}).reset_index()

# Set up connection to MySQL database
try:
    connection = mysql.connector.connect(
        host="qntm.mysql.database.azure.com",
        user="harrison",
        password="Welc0meT0Q!!",
        database="testdb"
    )
    print("Connection established successfully.")
except mysql.connector.Error as error:
    print("Error: Unable to connect to MySQL database.", error)

# Create table and insert data
try:
    cursor = connection.cursor()
    # Define columns and data types for the table
    create_table_query = '''CREATE TABLE IF NOT EXISTS contacts (
                            Company VARCHAR(255) PRIMARY KEY,
                            Internal_contact_1 TEXT,
                            Role_1 TEXT,
                            External_contact_1 TEXT,
                            Internal_contact_2 TEXT,
                            Role_2 TEXT,
                            External_contact_2 TEXT,
                            Internal_contact_3 TEXT,
                            Role_3 TEXT,
                            External_contact_3 TEXT,
                            Internal_contact_4 TEXT,
                            Role_4 TEXT,
                            External_contact_4 TEXT,
                            Internal_contact_5 TEXT,
                            Role_5 TEXT,
                            External_contact_5 TEXT
                            )'''
    # Execute the create table query
    cursor.execute(create_table_query)
    
    # Insert or update data into the table
    for row in contacts_df.itertuples(index=False):
        # Check if the row already exists in the table
        cursor.execute('''SELECT Company FROM contacts WHERE Company=%s''', (row[0],))
        result = cursor.fetchone()
        
        if result:
            # If the row already exists, update its values
            cursor.execute('''UPDATE contacts SET 
                                Internal_contact_1=%s,
                                Role_1=%s,
                                External_contact_1=%s,
                                Internal_contact_2=%s,
                                Role_2=%s,
                                External_contact_2=%s,
                                Internal_contact_3=%s,
                                Role_3=%s,
                                External_contact_3=%s, 
                                Internal_contact_4=%s,
                                Role_4=%s,
                                External_contact_4=%s,
                                Internal_contact_5=%s,
                                Role_5=%s,
                                External_contact_5=%s
                                WHERE Company=%s''', 
                           (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                             row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[0]))
        else:
            # If the row doesn't exist, insert it
            cursor.execute('''INSERT INTO contacts (
                                Company,
                                Internal_contact_1,
                                Role_1,
                                External_contact_1,
                                Internal_contact_2,
                                Role_2,
                                External_contact_2,
                                Internal_contact_3,
                                Role_3,
                                External_contact_3, 
                                Internal_contact_4,
                                Role_4,
                                External_contact_4,
                                Internal_contact_5,
                                Role_5,
                                External_contact_5
                            ) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', row)
    
    # Commit the changes to the database
    connection.commit()
    print("Data inserted or updated successfully into MySQL table.")
except mysql.connector.Error as error:
    print("Error: Unable to insert or update data into MySQL table.", error)

# Close the cursor and connection
cursor.close()
connection.close()
print("MySQL connection is closed.")