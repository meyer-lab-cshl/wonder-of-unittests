# The Wonder of Unittests

- How do you know your code is correct?

- Tests _encapsulate desired behaviour_:

~~~python
def add(a, b):
  return a + b

assert add(1, 1) == 2
~~~

## External test suite

`library.py`:

~~~python
def add(a, b):
  return a + b
~~~

`test_add.py`:

~~~python
import unittest
from library import add

class TestAdd(unittest.TestCase):

  def test_one_plus_one(self):
    """One plus one is two."""
    self.assertEqual(2, add(1, 1))

if __name__ == "__main__":
  unittest.main()
~~~

---

## Always write a _failing_ test

---

## angle.py

---

## Assert methods

~~~python
assertEqual(a, b)
assertFalse(x)
assertIs(a, b)
assertIsNotNone(x)
assertNotIn(a, b)
assertIsInstance(a, b)
assertWarns(warning, regex, callable, *args, **kwargs)
~~~

Plenty more... [https://docs.python.org/3.8/library/unittest.html?highlight=unittest#assert-methods](https://docs.python.org/3.8/library/unittest.html?highlight=unittest#assert-methods)

## Tests for _data_

~~~python
import unittest
import pandas as pd

class TestData(self):

  def test_number_of_rows(self):
    """The data should have 5,742 rows."""
    df = pd.read_csv("path/to/data.csv")
    self.assertEqual(5_742, len(df), "Data should have 5,742 rows.")

if __name__ == "__main__":
  unittest.main()
~~~

---
