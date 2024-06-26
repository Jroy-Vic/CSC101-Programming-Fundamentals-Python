import data

# Roy Vicerra

# Write your functions for each part in the space below.

# Part 1
# Purpose: this function takes in a list of data.CountyDemographics objects
#          and returns the total 2014 Population across the set of counties
#          in the provided list.
# Input: list[data.CountyDemographics]
# Output: int
# Example Input: full_data
# Example Output: 318857056

def population_total(data: list[data.CountyDemographics]) -> int:
    population = 0
    for demographics in data:
        population = population + demographics.population.get("2014 Population")
    return population

# Part 2
# Purpose: this function takes in two inputs, one being a list of data.CountyDemographics
#          objects and a string of a two-letter state abbreviation; returns a list
#          of data.CountyDemographics objects from the input that are within the specified state.
# Input: list[data.CountyDemographics], str
# Output: list[data.CountyDemographics]
# Example Input: reduced_data
# Example Output: [data.CountyDemographics(
#         {'Percent 65 and Older': 17.5,
#          'Percent Under 18 Years': 18.1,
#          'Percent Under 5 Years': 4.8},
#         'San Luis Obispo County',
#         {"Bachelor's Degree or Higher": 31.5,
#          'High School or Higher': 89.6},
#         {'American Indian and Alaska Native Alone': 1.4,
#          'Asian Alone': 3.8,
#          'Black Alone': 2.2,
#          'Hispanic or Latino': 22.0,
#          'Native Hawaiian and Other Pacific Islander Alone': 0.2,
#          'Two or More Races': 3.4,
#          'White Alone': 89.0,
#          'White Alone, not Hispanic or Latino': 69.5},
#         {'Per Capita Income': 29954,
#          'Persons Below Poverty Level': 14.3,
#          'Median Household Income': 58697},
#         {'2010 Population': 269637,
#          '2014 Population': 279083,
#          'Population Percent Change': 3.5,
#          'Population per Square Mile': 81.7},
#         'CA'),
#     data.CountyDemographics(
#         {'Percent 65 and Older': 11.5,
#          'Percent Under 18 Years': 21.7,
#          'Percent Under 5 Years': 5.8},
#         'Yolo County',
#         {"Bachelor's Degree or Higher": 37.9,
#          'High School or Higher': 84.3},
#         {'American Indian and Alaska Native Alone': 1.8,
#          'Asian Alone': 13.8,
#          'Black Alone': 3.0,
#          'Hispanic or Latino': 31.5,
#          'Native Hawaiian and Other Pacific Islander Alone': 0.6,
#          'Two or More Races': 5.0,
#          'White Alone': 75.9,
#          'White Alone, not Hispanic or Latino': 48.3},
#         {'Per Capita Income': 27730,
#          'Persons Below Poverty Level': 19.1,
#          'Median Household Income': 55918},
#         {'2010 Population': 200849,
#          '2014 Population': 207590,
#          'Population Percent Change': 3.4,
#          'Population per Square Mile': 197.9},
#         'CA')], "CA"

def filter_by_state(data: list[data.CountyDemographics], state_abbreviation: str) -> list[data.CountyDemographics]:
    state_data = []
    for demos in data:
        if demos.state == state_abbreviation:
            state_data.append(demos)
    return state_data

# Part 3
# Purpose: this function takes two inputs, a list of data.CountyDemographics objects
#          and the education key of interest; returns the total 2014 sub-population across the set
#          of counties.
# Input: list[data.CountyDemographics], str
# Output: float
# Example Input: reduced_data, "Bachelor's Degree or Higher"
# Example Output: 195114.09100000001

def population_by_education(data: list[data.CountyDemographics], education: str) -> float:
    try:
        total_pop = 0
        for demos in data:
            if education not in demos.education:
                return total_pop
            else:
                ratio = demos.education.get(education)
                percentage = ratio / 100
                sub_pop = demos.population.get("2014 Population") * percentage
                total_pop = sub_pop + total_pop
        return total_pop
    except ZeroDivisionError:
        print("NO DATA FOUND")
        exit()

# Purpose: this function takes two inputs, a list of data.CountyDemographics objects
#          and the ethnicity key of interest; returns the total 2014 sub-population across the set
#          of counties.
# Input: list[data.CountyDemographics], str
# Output: float
# Example Input: reduced_data, "Two or More Races"
# Example Output: 23613.951

def population_by_ethnicity(data: list[data.CountyDemographics], ethnicity: str) -> float:
    try:
        total_pop = 0
        for demos in data:
            if ethnicity not in demos.ethnicities:
                return total_pop
            else:
                ratio = demos.ethnicities.get(ethnicity)
                percentage = ratio / 100
                sub_pop = demos.population.get("2014 Population") * percentage
                total_pop = sub_pop + total_pop
        return total_pop
    except ZeroDivisionError:
        print("NO DATA FOUND")
        exit()

# Purpose: this function takes a list of data.CountyDemographics objects and returns
#          the total 2014 sub-population indicated by income key across the set of counties.
# Input: list[data.CountyDemographics]
# Output: float
# Example Input: reduced_data
# Example Output: 107711.714

def population_below_poverty_level(data: list[data.CountyDemographics]) -> float:
    try:
        total_pop = 0
        for demos in data:
            ratio = demos.income.get("Persons Below Poverty Level")
            percentage = ratio / 100
            sub_pop = demos.population.get("2014 Population") * percentage
            total_pop = total_pop + sub_pop
        return total_pop
    except ZeroDivisionError:
        print("NO DATA FOUND")
        exit()


# Part 4
# Purpose: this function takes two inputs, a list of data.CountyDemographics objects and the
#          education key of interest; returns the specified 2014 sub-population percentage of
#          the total 2014 population.
# Input: list[data.CountyDemographics], str
# Output: float
# Example Input: reduced_data, "Bachelor's Degree or Higher"
# Example Output: 29.751482663503165

def percent_by_education(data: list[data.CountyDemographics], education: str) -> float:
    try:
        sub_pop = population_by_education(data, education)
        tot_pop = population_total(data)
        percentage = (sub_pop / tot_pop) * 100
        return percentage
    except ZeroDivisionError:
        print("NO DATA FOUND")
        exit()

# Purpose: this function takes two inputs, a list of data.CountyDemographics objects and the
#          ethnicity key of interest; returns the specified 2014 sub-population percentage of
#          the total 2014 population.
# Input: list[data.CountyDemographics], str
# Output: float
# Example Input: reduced_data, "Two or More Races"
# Example Output: 3.6007140755062803

def percent_by_ethnicity(data: list[data.CountyDemographics], ethnicity: str) -> float:
    try:
        sub_pop = population_by_ethnicity(data, ethnicity)
        tot_pop = population_total(data)
        percentage = (sub_pop / tot_pop) * 100
        return percentage
    except ZeroDivisionError:
        print("NO DATA FOUND")
        exit()

# Purpose: this function takes one input, a list of data.CountyDemographics objects,
#          and returns the 2014 sub-population indication by income key as a percentage of
#          the total 2014 population.
# Input: list[data.CountyDemographics], str
# Output: float
# Example Input: reduced_data
# Example Output: 16.424150481920915

def percent_below_poverty_level(data: list[data.CountyDemographics]) -> float:
    try:
        sub_pop = population_below_poverty_level(data)
        tot_pop = population_total(data)
        percentage = (sub_pop / tot_pop) * 100
        return percentage
    except ZeroDivisionError:
        print("NO DATA FOUND")
        exit()

# Part 5
# Purpose: these two functions each take three inputs: 1) a list of data.CountyDemographics
#          objects, 2) the education key of interest, and 3) a numeric threshold number; return
#          a list of all data.CountyDemographics objects for which the value for the specified key
#          is greater than or less than the specified threshold value.
# Input: list[data.CountyDemographics], str, float
# Output: list[data.CountyDemographics]
# Example Input: reduced_data, "Bachelor's Degree or Higher", 60
# Example Output: []

def education_greater_than(data: list[data.CountyDemographics], edu: str, threshold: float) -> list[data.CountyDemographics]:
    result_data = []
    for demos in data:
        if edu in demos.education:
            if demos.education.get(edu) > threshold:
                result_data.append(demos)
    return result_data

def education_less_than(data: list[data.CountyDemographics], edu: str, threshold: float) -> list[data.CountyDemographics]:
    result_data = []
    for demos in data:
        if edu in demos.education:
            if demos.education.get(edu) < threshold:
                result_data.append(demos)
    return result_data

# Purpose: these two functions each take three inputs: 1) a list of data.CountyDemographics
#          objects, 2) the ethnicity key of interest, and 3) a numeric threshold number; return
#          a list of all data.CountyDemographics objects for which the value for the specified key
#          is greater than or less than the specified threshold value.
# Input: list[data.CountyDemographics], str, float
# Output: list[data.CountyDemographics]

def ethncitiy_greater_than(data: list[data.CountyDemographics], eth: str, threshold: float) -> list[data.CountyDemographics]:
    result_data = []
    for demos in data:
        if eth in demos.ethnicities:
            if demos.ethnicities.get(eth) > threshold:
                result_data.append(demos)
    return result_data

def ethnicity_less_than(data: list[data.CountyDemographics], eth: str, threshold: float) -> list[data.CountyDemographics]:
    result_data = []
    for demos in data:
        if eth in demos.ethnicities:
            if demos.ethnicities.get(eth) < threshold:
                result_data.append(demos)
    return result_data

# Purpose: these two functions both take two inputs: 1) a lst of data.CountyDemographics
#          objects and 2) a numerical threshold value; return a list of all data.CountyDemographics
#          objects for which the value for key "Persons Below Poverty Level" is greater than or less
#          than the specified threshold value.
# Input: list[data.CountyDemographics], float
# Output: list[data.CountyDemographics]

def below_poverty_level_greater_than(data: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    result_data = []
    for demos in data:
        if demos.income.get("Persons Below Poverty Level") > threshold:
            result_data.append(demos)
    return result_data

def below_poverty_level_less_than(data: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    result_data = []
    for demos in data:
        if demos.income.get("Persons Below Poverty Level") < threshold:
            result_data.append(demos)
    return result_data