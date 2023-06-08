import pandas as pd
import numpy as np
import mysql.connector
from mysql.connector import Error

file_path = r'C:\Users\New User\Segmentation\Data\DataCSV.xlsx'
data_df = pd.read_excel(file_path, sheet_name= 'Master')

def concat_notes(notes):
    notes = notes.dropna().astype(str).str.strip() # drop empty rows, convert to string, and strip whitespace
    notes = notes[notes != ''] # drop empty strings
    if len(notes) == 0:
        return 'No notes.' # return empty string if there are no notes
    else:
        return ''.join(notes) # join the notes with a space separator



aggregated_df = data_df.groupby('Company').agg({
    'Priority': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Industry': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Region': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Previously Worked With Them': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Open Opp': lambda x: ', '.join(pd.Series(x).dropna().astype(str)), 
    'QC Team': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'QC Paper': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Papers': lambda x: ', '.join(pd.Series(x).dropna().astype(str)), 
    'Links': lambda x: ', '.join(pd.Series(x).dropna().astype(str)), 
    'Engaged with': lambda x: ', '.join(pd.Series(x).dropna().astype(str)), 
    'Articles': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Article Links': lambda x: ', '.join(pd.Series(x).dropna().astype(str)),
    'Notes': concat_notes
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
    create_table_query = '''CREATE TABLE IF NOT EXISTS aggregated_data (
                            Company VARCHAR(255) PRIMARY KEY,
                            Priority TEXT,
                            Industry TEXT,
                            Region TEXT,
                            Previously_Worked_With_Them TEXT,
                            Open_Opp TEXT,
                            QC_Team TEXT,
                            QC_Paper TEXT,
                            Papers TEXT,
                            Links TEXT,
                            Engaged_with TEXT,
                            Articles TEXT,
                            Article_Links TEXT,
                            Notes TEXT
                            )'''
    # Execute the create table query
    cursor.execute(create_table_query)
    
    # Insert or update data into the table
    for row in aggregated_df.itertuples(index=False):
        # Check if the row already exists in the table
        cursor.execute('''SELECT Company FROM aggregated_data WHERE Company=%s''', (row[0],))
        result = cursor.fetchone()
        
        if result:
            # If the row already exists, update its values
            cursor.execute('''UPDATE aggregated_data SET 
                                Priority=%s, 
                                Industry=%s, 
                                Region=%s, 
                                Previously_Worked_With_Them=%s, 
                                Open_Opp=%s,
                                QC_Team=%s,
                                QC_Paper=%s, 
                                Papers=%s, 
                                Links=%s, 
                                Engaged_with=%s, 
                                Articles=%s, 
                                Article_Links=%s, 
                                Notes=%s 
                                WHERE Company=%s''', 
                           (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[0]))
        else:
            # If the row doesn't exist, insert it
            cursor.execute('''INSERT INTO aggregated_data (
                                Company,
                                Priority,
                                Industry,
                                Region,
                                Previously_Worked_With_Them,
                                Open_Opp,
                                QC_Team,
                                QC_Paper,
                                Papers,
                                Links,
                                Engaged_with,
                                Articles,
                                Article_Links,
                                Notes
                            ) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', row)
    
    # Commit the changes to the database
    connection.commit()
    print("Data inserted or updated successfully into MySQL table.")
except mysql.connector.Error as error:
    print("Error: Unable to insert or update data into MySQL table.", error)

# Close the cursor and connection
cursor.close()
connection.close()
print("MySQL connection is closed.")

