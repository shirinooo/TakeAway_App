# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

---(Use theTwilio-python pkg for this)---

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Tyre:
    # User-facing properties:
    

    def __init__(self):
        # Parameters:
        #   name: string
        self.tyre_fl = [{"added_on": yy-mm-dd, "tyre_pressure": float, "tyre_tread_depth": float}]
        self.tyre_fr = {}
        self.tyre_bl = {}
        self.tyre_br = {}

        # Side effects:
        #   Sets the name property of the self object
        pass


    def update_tyre_readings(self, tyre_pressure, tyre_tread_depth, date):
        # Parameters:
        #   tyre_pressure
        #   tyre_tread_depth
        #   date
        # Returns:
        #   Nothing
        # Side-effects
        #   updating the tyres reading
        pass # No code here yet

    
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
