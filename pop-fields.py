# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# new.py
# Created on: 2018-09-13
#               by Patty Jula
# Description: Update schema for import preparation using a dictionary
#              and function.
# ---------------------------------------------------------------------------
# Import libraries
import os
import arcpy

# Set work space
arcpy.env.workspace = "C:/Users/UID/GIS/landbase.gdb"

# Local variables
pdtypefield= "TYPE"
pdmphfield= "SPEEDLIMIT"
fc = "centerline"

#--------------------------------------------------
# Process TYPE field
#Add type field
arcpy.AddField_management(fc, pdtypefield,'DOUBLE','','')

# Street type dictionary
# Query values from ST_DESIG field and define what new value should be
dict ={"ST_DESIG IN (12,13,14)" : 1200,"ST_DESIG IN (0,1,17,21,23,52,67)" : 1300, 
        "ST_DESIG IN (2,3,16,53)" : 1400, "ST_DESIG IN (4,5,15,22,54,55)" : 1500,
        "ST_DESIG IN (6,19,20,56)" : 1600, "ST_DESIG IN (7)" : 1110,
        "ST_DESIG IN (8)" : 1121,"ST_DESIG IN (9)" : 1122,
        "ST_DESIG IN (11)" : 4000}
        
# Create a function to utilize dict values
def update_type(where_clause, new_val):
    # Open an update cursor
    with arcpy.da.UpdateCursor(fc, [pdtypefield], where_clause) as cursor:
        for row in cursor:
            # Get value and update row
            row[0]= new_val
            cursor.updateRow(row)

# Loop through dictionary and call function update_type
for where_clause, new_val in dict.items():
	update_type(where_clause, new_val)

#--------------------------------------------------
# Process MPH field
# Add MPH field
arcpy.AddField_management(fc, pdmphfield,'LONG','','')

# MPH dictionary
# Note TBM types 3100 and 3200 are not coded
mphdict ={"ST_DESIG IN (12,13)" : 40,"ST_DESIG IN (14)" : 45, 
        "ST_DESIG IN (0,1,2,3,16,17,23,52,53,67)" : 35, "ST_DESIG IN (21)" : 40,
        "ST_DESIG IN (4,5,15,19,22,54,55)" : 25,"ST_DESIG IN (6,20,56)" : 15,
        "ST_DESIG IN (7)" : 60,"ST_DESIG IN (8)" : 45,"ST_DESIG IN (9)" : 45,
        "ST_DESIG IN (11)" : 1}
        
def update_mph(where_clause, new_val):
    with arcpy.da.UpdateCursor(fc, [pdmphfield], where_clause) as cursor:
        for row in cursor:
            # Get value and update row
            row[0]= new_val
            cursor.updateRow(row)
	
# Loop through mphdict and update field with function update_mph
for where_clause, new_val in mphdict.items():
    update_mph(where_clause, new_val)
