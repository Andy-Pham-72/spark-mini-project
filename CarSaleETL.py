
def extract_vin_key_value(row):
    """
    This method maps vin_number, make, year, and incident_type from the corresponding row
    
    :param row: Row of each column
    :return: The key, value pair in the tuple type of dictionary as each record.
        eg: [('VXIO456XLBB630221', ('Nissan', '2003', 'I')),
             ('VOME254OOXW344325', ('Mercedes', '2015', 'I'))]
    """
    row_sep = row.split(",")
    
    # assign vin number
    vin_num = row_sep[2]
    # asign car maker
    make = row_sep[3]
    # assign manufacture year
    year = row_sep[5]
    # assign type of incident
    incident_type = row_sep[1]
    
    return (vin_num , (make, year, incident_type))

def populate_make(vals):
    """
    This method sorts all the vin numbers and fills all the corresponding rows of make and year columns
    with the incident_type to an output list
    
    :param vals: Values from the key-value pair (followed after groupByKey())
    :return: Lists of make, year, and incident_type
        eg: [('Nissan', '2003', 'I'),
             ('Nissan', '2003', 'A'),]
    """
    list_val = []
    for val in vals:
        # iterate through the list and append if make value exists
        if val[0] != '' :
            make = val[0]
        # iterate through the list and append if year value exists
        if val[1] != '' :
            year = val[1]
        # append make, year and incident_type which is 'val[2]'
        list_val.append((make, year, val[2]))
    return list_val

def extract_make_key_value(list_val):
    """
    This method obtains make and year from the list produced by populate_make() method
    and it only counts if the incident_type == "A"
    
    :param list_val: list of the output from populate_make() method with the format as (make, year, incident_type)
    :return: a tuple type
        eg: [('Nissan-2003', 0),
             ('Nissan-2003', 1),]
             
    """
    
    if list_val[2] == "A":
        return list_val[0]+ '-' + list_val[1], 1
    else:
        return list_val[0]+ '-' + list_val[1], 0