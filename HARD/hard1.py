import re

def is_valid_number(s):
   
    regex = re.compile(r"""
        ^                             
        [+-]?                       
        (                             
            (\d+\.\d*|\.\d+|\d+\.\d+) 
            (e[+-]?\d+)?              
            |                         
            \d+                       
            (e[+-]?\d+)?              
        )
        $                             
    """, re.VERBOSE | re.IGNORECASE)

    return bool(regex.match(s))

# Test cases
test_cases = [
    "123", "+123", "-123", "123.456", "-123.456", ".456", "123.", "123e456", "123E456", 
    "123.456e789", "-123.456E789", ".456e789", "123.e789", "+123.456E-789", 
    "abc", "123e", "e123", "123.456.789", "+-123", "123 456"
]

for test in test_cases:
    print(f"'{test}': {is_valid_number(test)}")
