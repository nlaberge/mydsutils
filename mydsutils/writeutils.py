#!/usr/bin/env python
import re
import datetime

def write_variable_line(variable_name, variable_value, notes):
    date_and_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return  "\\newcommand\\"+variable_name+"{"+str(variable_value)+"}"+ " % " + date_and_time + '; ' + notes

def update_variables_file(path,variable_name,variable_value, notes = '', add_commas = False):
    '''
    Updates a tex file containing variables to be used in the paper.
    If the variable is not in the file already, it is added.
    '''
    # update variable_value according to params
    if add_commas:
        variable_value = "{:,}".format(variable_value)
    
    # read tex file
    with open(path, "r") as f:
        f_lines = f.read().split('\n')
        var_in_file = False
        # check to see if variable is in file
        for i, line in enumerate(f_lines):
            line_var_name_search = re.search(r'newcommand\\(.*?){', line)
            if line_var_name_search is not None:
                line_var_name = line_var_name_search.group(1)
                if line_var_name == variable_name: # variable exists in file
                    f_lines[i] = write_variable_line(variable_name, variable_value, notes)   # update the variable value
                    var_in_file = True
                    print(f'{variable_name} updated in {path}')
                    break
        if not var_in_file:
            f_lines.append(write_variable_line(variable_name, variable_value, notes))
            print(f'{variable_name} added to {path}')
    f_lines_updated = '\n'.join(f_lines)
    # write updated tex file
    with open(path, "w") as f:
        f.write(f_lines_updated)
    
