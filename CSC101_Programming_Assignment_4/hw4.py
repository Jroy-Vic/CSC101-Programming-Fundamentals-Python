import build_data
import sys
import hw3

# Roy Vicerra

# Task 1


# Purpose: extract the commands of an operations file.
# Input: path of the operations file (str)
# Output: list of commands (list[str])
#         (where each string represents a single command)

def extract_commands(ops_file_path):
    try:
        with open(ops_file_path) as file:
            contents = file.read()

        list_contents = contents.split('\n')
        return list_contents
    except FileNotFoundError:
        print("ERROR: operation file does not exist. Please input new '.ops' file.")
        exit()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: extract each part of a command.
# Input: str (represents a single command)
# Output: dict
#         Examples:
# filter-gt/filter-lt: {"operation": str, "field": str, "number": float}
# filter-state:        {"operation": str, "state abbreviation": str}
# display:             {"operation": str}

def extract_command_parts(some_command):
    list_commands = some_command.split(':')
    operation = list_commands[0]
    ops_dict = {"Operation": operation}

    if len(list_commands) == 2 and len(list_commands[1]) == 2:
        ops_dict["State Abbreviation"] = list_commands[1]
    elif len(list_commands) >= 2:
        ops_dict["Field"] = list_commands[1]
        if len(list_commands) == 3:
            try:
                ops_dict["Number"] = float(list_commands[2])
            except ValueError:
                print("ERROR: number is invalid. Please input a valid number.")
                return None

    return ops_dict


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


display_list = []

# Purpose: processes the operation inputted in the command-line argument;
#          returns the filtered/processed data provided.
# Input: str (command), list (dataset)
# Output: list[data.CountyDemographics]

def run_command(command_in, dataset):
    operation = com_dict.get("Operation")

    if operation == "filter-state":
        state_abbreviation = com_dict.get("State Abbreviation")
        state_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
                      "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NE", "NV", "NH", "NJ", "NM", "NY", "NC",
                      "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        if state_abbreviation in state_list:
            filtered_county_list = hw3.filter_by_state(dataset, state_abbreviation)
            display_list.append(filtered_county_list)
            return "Filter: state == {} ({} entries)".format(state_abbreviation, len(filtered_county_list))
        else:
            return "ERROR: state abbreviation is invalid. Please input a valid state abbreviation."


    elif operation == "filter-gt" or operation == "filter-lt" or operation == "population" or operation == "percent":
        field = com_dict.get("Field")
        field_type = field.split('.')[0]
        field_key = field.split('.')[1]
        field_key_list = ["Bachelor's Degree or Higher", "High School or Higher", "American Indian and Alaska Native Alone",
                          "Asian Alone", "Black Alone", "Hispanic or Latino", "Native Hawaiian and Other Pacific Islander Alone",
                          "Two or More Races", "White Alone", "White Alone, not Hispanic or Latino", "Persons Below Poverty Level"]

        if operation == "filter-gt" and field_key in field_key_list:
            number = com_dict.get("Number")
            if field_type == "Education":
                filtered_county_list = hw3.education_greater_than(dataset, field_key, number)
            elif field_type == "Ethnicities":
                filtered_county_list = hw3.ethncitiy_greater_than(dataset, field_key, number)
            elif field_type == "Income":
                filtered_county_list = hw3.below_poverty_level_greater_than(dataset, number)
            else:
                return "ERROR: field type is invalid. Please input a valid field type."
            display_list.append(filtered_county_list)
            return "Filter: '{}' gt {} ({} entries)".format(field, number, len(filtered_county_list))

        elif operation == "filter-lt" and field_key in field_key_list:
            number = com_dict.get("Number")
            if field_type == "Education":
                filtered_county_list = hw3.education_less_than(dataset, field_key, number)
            elif field_type == "Ethnicities":
                filtered_county_list = hw3.ethnicity_less_than(dataset, field_key, number)
            elif field_type == "Income":
                filtered_county_list = hw3.below_poverty_level_less_than(dataset, number)
            else:
                return "ERROR: field type is invalid. Please input a valid field type."
            display_list.append(filtered_county_list)
            return "Filter: '{}' lt {} ({} entries)".format(field, number, len(filtered_county_list))

        elif operation == "population" and field_key in field_key_list:
            if field_type == "Education":
                filtered_county_pop = hw3.population_by_education(dataset, field_key)
            elif field_type == "Ethnicities":
                filtered_county_pop = hw3.population_by_ethnicity(dataset, field_key)
            elif field_type == "Income":
                filtered_county_pop = hw3.population_below_poverty_level(dataset)
            else:
                return "ERROR: field type is invalid. Please input a valid field type."
            return "2014: '{}' population: {}".format(field, int(filtered_county_pop))

        elif operation == "percent" and field_key in field_key_list:
            if field_type == "Education":
                filtered_county_percent = hw3.percent_by_education(dataset, field_key)
            elif field_type == "Ethnicities":
                filtered_county_percent = hw3.percent_by_ethnicity(dataset, field_key)
            elif field_type == "Income":
                filtered_county_percent = hw3.percent_below_poverty_level(dataset)
            else:
                return "ERROR: field type is invalid. Please input a valid field type."
            return "2014: '{}' percentage: {} %".format(field, round(filtered_county_percent, 3))

        else:
            return "ERROR: field key is invalid. Please input a valid field key."


    elif operation == "population-total":
        total_pop = hw3.population_total(dataset)
        return "2014 Population: {}".format(total_pop)


    elif operation == "display":
        for county_list in display_list:
            for display_val in county_list:
                print("{}, {}\n" \
                "       Population: {}\n" \
                "       Age:\n" \
                "               < 5: {}%\n" \
                "               < 18: {}%\n" \
                "               > 65: {}%\n" \
                "       Education:\n" \
                "               >= High School: {}%\n" \
                "               >= Bachelor's: {}%\n" \
                "       Ethnicity Percentages:\n" \
                "               American Indian and Alaska Native: {}%\n" \
                "               Asian Alone: {}%\n" \
                "               Black Alone: {}%\n" \
                "               Hispanic or Latino: {}%\n" \
                "               Native Hawaiian and Other Pacific Islander Alone: {}%\n" \
                "               Two or More Races: {}%\n" \
                "               White Alone: {}%\n" \
                "               White Alone, not Hispanic or Latino: {}%\n" \
                "       Income:\n" \
                "               Median Household: {}\n" \
                "               Per Capita: {}\n" \
                "               Below Poverty Level: {}%\n".format(display_val.county, display_val.state, display_val.population["2014 Population"],
                                                            display_val.age["Percent Under 5 Years"], display_val.age["Percent Under 18 Years"],
                                                            display_val.age["Percent 65 and Older"], display_val.education["High School or Higher"],
                                                            display_val.education["Bachelor's Degree or Higher"],
                                                            display_val.ethnicities["American Indian and Alaska Native Alone"],
                                                            display_val.ethnicities["Asian Alone"], display_val.ethnicities["Black Alone"],
                                                            display_val.ethnicities["Hispanic or Latino"],
                                                            display_val.ethnicities["Native Hawaiian and Other Pacific Islander Alone"],
                                                            display_val.ethnicities["Two or More Races"], display_val.ethnicities["White Alone"],
                                                            display_val.ethnicities["White Alone, not Hispanic or Latino"],
                                                            display_val.income["Median Household Income"], display_val.income["Per Capita Income"],
                                                            display_val.income["Persons Below Poverty Level"]))
            print("~~~~~~~~~~~~~~~~~~\n")


    else:
        return "ERROR: operation is invalid. Please input a valid operation."


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: using command-line arguments, perform specific operations to manipulate
#          the data found in the CountyDemographics dataset; if argument is incomplete
#          or cannot be processed, return an error message and continue processing or
#          exit the program depending on the scenario.
# Input: '.ops' file
# Output: str

if __name__ == '__main__':
    full_data = build_data.get_data()
    len_data = len(full_data)
    entries = ("{} records loaded").format(len_data)
    print(entries)

    user_input = sys.argv
    ops_file = user_input[1]
    path_ops_file = "./inputs/" + ops_file
    ops_commands = extract_commands(path_ops_file)

    count = 0
    for commands in ops_commands:
        try:
            if commands != '':

                com_dict = extract_command_parts(commands)
                if com_dict != None:
                    processed_data = run_command(com_dict, full_data)
                    if processed_data != None:
                        print(processed_data)
                try:
                    full_data = display_list[count]
                    count = count + 1
                except IndexError:
                    continue

        except TypeError:
            print("ERROR: too many commands were inputted. Please input the correct parameters.")
            continue