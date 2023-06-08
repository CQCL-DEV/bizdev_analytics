import pandas as pd
import numpy as np
import mysql.connector
from mysql.connector import Error

from docxtpl import DocxTemplate

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

# Load data into pandas dataframes and convert to array
agg_df = pd.read_sql_query('SELECT * FROM aggregated_data', connection)
cont_df = pd.read_sql_query('SELECT * FROM contacts', connection)

# Merge data frames with all data
merged_df = agg_df.merge(cont_df, on='Company', how='outer')
merged_df = merged_df.fillna('')

# Get a list of the unique company names
company_names = merged_df['Company'].unique()

# Load the template file
template_path = r'C:\Users\New User\Segmentation\Template\template.docx'
template = DocxTemplate(template_path)


#Creates a report based on the template
#for i, company_name in enumerate(company_names[0:2]):    #for companies between i an j
for company_name in company_names: #for all companies in the database
    # Filter the dataframe for the current company
    company_df = merged_df[merged_df['Company'] == company_name]
    
    # Convert the company dataframe to a dictionary of records
    context = company_df.to_dict('records')
    
    # Render the template with the current company's data
    template.render(context[0])
    
    # Define the file path and name to save the generated document
    file_path = r'C:\Users\New User\Segmentation\Reports\{}_{}.docx'.format(company_name, 'report')
    
    # Save the generated document to the new file with the company name and index as the file name
    template.save(file_path)



