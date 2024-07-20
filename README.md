# mb_internTask

## Description
**mb_internTask** is a project focused on the calculation of plane figure squares. It provides a factory to get different figure implementations and calculate their squares.

## Usage
To use the project, follow these steps:

1. Use the figure factory to get the figure implementation.
2. Call the `get_square` function on the figure implementation to calculate the square.

## Project requirements
Python > 3.9
pytest - for tests

## Extension
To extend the project by adding a new figure, follow these steps:

1. Define a new figure class inherited from the abstract class `Figure`.
2. Override the following functions:
   - `get_square`: Implement the logic to calculate the square of the figure.
   - `validate_arguments`: Implement the logic to validate the arguments provided to the figure. Default case - pass the arguments to the super class.
   - `__str__`: Implement the string representation of the figure.

## Example
```python
from figures.FigureFactory import FigureFactory

# Get a figure implementation (e.g., Circle, Square, etc.)
figure_1 = FigureFactory.get_impl(2, 3, 4)

# Calculate the square
square = figure_1.get_square()
print(f'The square of the figure is: {square}')
