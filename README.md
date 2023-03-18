# PLANEKS-Test-task
Web-service for generating CSV files with fake (dummy) data using Python and Django.

# Description
Any logged-in user(any user can log in to the system with a username and password) 
can create any number of data schemas to create datasets with fake data.
Each such data schema has a name and a list of columns with names and
specified data types. Users can build the data schema with any number of columns 
of any type by theirs choice.
Each column also has its own name (which will be a column header in the
CSV file) and order (just a number to manage column order).
After creating the schema, the user should be able to input the number of
records he/she needs to generate and press the “Generate data” button and download 
it later if they wish.

