# ignacious-iterator

## Summary
Automate populating schema in update feature class so it can be easily imported to production dataset

## Need for script
This script was developed out of a need to import records from one attribute table to a production dataset, where the two datasets have different schemas. Aside from differing schemas, the field values require translation. For example, the value 5 in the source data needs to be populated as 1500 in the production dataset. The Python [script](https://stackoverflow.com/questions/19314342/python-sqlalchemy-pass-parameters-in-connection-execute) in this repository prepares the update feature class so it is ready to "append" to the production feature class. 

The method presented here does not represent the best, or only, method to prepare data for import to another dataset. 

## Script steps

First, the script will add a new field to the update feature class matching the field name in the production feature class, then it will query a field in the update feature class and update that new field with the required value. For example, if a field in the update feature class contains the value 5, it might be required to contain the value 1500 in the production feature class.

This script contains the SQL statement and the new values within a dictionary. A function, called ```update_type```, uses an UpdateCursor to complete the processing for the key, value pairs in the dictionary.  A for loop calls these key, values pairs and instantiates the function.

The first dictionary and script process street type. A similar process, creating a dictionary and function, is setup to populate speed limit values. This script demonstrates value of resusable code to automate otherwise tedious processes.
