NoneType = type(None)

class NoDatabaseSelected(Exception): pass
class InvalidData(Exception): pass
class InvalidVersion(Exception): pass

def is_valid(input_data, structure):
    "Check two data structures to verify that the input data is correct."
    warnings = []
    errors = []
    
    # Check each field in the input data
    for input_field in input_data:
        
        # If the field is in the stored data, then continue validating
        if input_field in structure:
            input_type = type(input_data[field])
            field_type = structure[input_field]
            
            # If the field types are valid, continue.
            if input_type == field_type or input_type == NoneType:
                continue;
            
            # If it isn't, then there is an issue.
            else:
                error = "{0} of type {1} is not {2}".format(
                    input_field,
                    input_type,
                    field_type
                )
                errors.append(error)
        
        # If it's not in the stored data, then an unexpected field was added.
        else:
            warning = "{0} not in structure.".format(input_field)
            warnings.append(warning)
    
    return {
        'errors': errors,
        'warnings': warnings,
    }

def type_valid(input_data, data_type):
    "Check a variable to see if it is the right data type."
    if type(input_data) == data_type:
        return True
    
    return False
