## Testing Your Code
import unittest

# Testing a function
# Generating function
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

# testing function
print("Enter 'q' at any point to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")


# unit tests and test cases
# a passing test
# import unittest (refer to the top)
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus'
        )
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main(exit=False) # exit=False to prevent closing

# try it yourself
# 11-1 City, Country
def city_country(city, country):
    string = f"{city.title()}, {country.title()}"
    return string

print(city_country('Accra', 'Ghana'))

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        """Do inputs like Accra, Ghana work?"""
        test = city_country('Accra', 'Ghana')
        self.assertEqual(test, 'Accra, Ghana')

unittest.main(exit=False)

# 11-2 Population
def city_country(city, country, population = 0):
    if population:
        string = f"{city.title()}, {country.title()} - population {int(population)}"
    else:
        string = f"{city.title()}, {country.title()}"
    return string

print(city_country('Accra', 'Ghana', 3000000))

class CityCountryTestCase(unittest.TestCase):
    def test_city_country_population(self):
        """Do inputs like Accra, Ghana - population 3000000 work?"""
        test = city_country('Accra', 'Ghana', 3000000)
        self.assertEqual(test, 'Accra, Ghana - population 3000000')

unittest.main(exit=False)

# testing a class
# A class to test
class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""
    
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the survey question."""
        print(question)
    
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
    
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)

# using the instance
# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

# testing if it works

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        
        self.assertIn('English', my_survey.responses)
    
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language dd you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main(exit='False')

# the setup method: allows us to have tests on standby
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, my_survey.responses)

unittest.main(exit='False')

# try it yourself
# 11-3 Employee

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        """Defining attributes for Employee class"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, salary_raise = 5000):
        """Give $5000 raise to Employee"""
        self.annual_salary = self.annual_salary + salary_raise
        return self.annual_salary

class TestEmployee(unittest.TestCase):
    """Test for class Employee"""
    def test_employee_salary(self):
        """Test that a salary is equal to the raised amount."""
        Employee('John', 'Doe', 15000)
        raised_salary = Employee.give_raise()
        self.assertEqual(raised_salary, 20000)

unittest.main(exit='False')