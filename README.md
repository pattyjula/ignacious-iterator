# ignacious-iterator

## Need for script

Sometimes in a GIS database, it is neccesary to import rows to a "production" feature class from the attribute table of an "update" feature class. These tables might contain different schemas. This (script)[https://stackoverflow.com/questions/19314342/python-sqlalchemy-pass-parameters-in-connection-execute] in this repository prepares the update feature class so it is ready to "append" to the production feature class. 

## Script steps

First, the script will add a new field to the update feature class matching the field name in the source feature class, then it will query a field in the update feature class and update that new field with the required value. For example, if a field in the update feature class contains the value 5, it might be required to contain the value 1500 in the production feature class.

This script contains the SQL statement and the new values within a dictionary. A function, called ```update_type```, uses an UpdateCursor to complete the processing for the key, value pairs in the dictionary.  A for loop calls these key, values pairs and instantiates the function.

The first dictionary and script process street type. A similar process, creating a dictionary and function, is setup to populate speed limit values. This script demonstrates value of resusable code.
