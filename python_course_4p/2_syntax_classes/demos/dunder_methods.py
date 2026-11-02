import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Class basics
    """)
    return


@app.class_definition
# Use class keyword to define a class
class Person:
    """Class for natural persons."""

    # Class attributes.

    name = "John"
    lastname = "Doe"

    # Class methods.

    # First argument is always self.
    def full_name(self):
        """Returns the person's full name."""

        # Use self to access attributes
        return f"{self.name} {self.lastname}"


@app.cell
def _():
    # Create an instance of the class.
    person1 = Person()
    return (person1,)


@app.cell
def _(person1):
    # Access attribute using <instance>.<attribute>.
    person1.name
    return


@app.cell
def _(person1):
    # Call methods using <instance>.<method>().
    person1.full_name()
    return


@app.cell
def _():
    # Create a second person.
    person2 = Person()
    return (person2,)


@app.cell
def _(person2):
    # Both share the same attributes...
    person2.full_name()
    return


@app.cell
def _(person1, person2):
    # But they are different objects.
    print("person1 id: ", id(person1))
    print("person2 id: ", id(person2))
    return


@app.cell
def _():
    # Override the class attribute value...
    Person.name = "Test"
    return


@app.cell
def _(person1, person2):
    # Changes all instances!
    print("person1 name: ", person1.name)
    print("person2 name: ", person2.name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dunder methods
    """)
    return


@app.class_definition
class DunderPerson:
    """Class for natural persons."""

    def __init__(self, name, lastname):
        self.name = name.capitalize()
        self.lastname = lastname.capitalize()

    def __str__(self):  
        """String representation of the person."""
        return self.full_name()
    
    def full_name(self):
        """Returns the person's full name."""
        return f"{self.name} {self.lastname}"


@app.cell
def _():
    # Names are provided by calling the constructor.
    jane = DunderPerson('jane', 'doe')
    return (jane,)


@app.cell
def _(jane):
    jane.full_name()
    return


@app.cell
def _(jane):
    # Print uses __str__ method.
    print(jane)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Vector2D
    """)
    return


@app.class_definition
class Vector2D:
  """Clas for managing 2D vectors."""

  def __init__(self, dx, dy):
    self.dx = dx
    self.dy = dy

  def __add__(self, other):
    return Vector2D(
      self.dx + other.dx,
      self.dy + other.dy
    )

  def __str__(self):
    return f"({self.dx}, {self.dy})"


@app.cell
def _():
    # Construct two vectors.
    v1 = Vector2D(4, 5)
    v2 = Vector2D(2, 4)
    return v1, v2


@app.cell
def _(v1, v2):
    # Add 2 vectors together; prints "6, 9".
    print(v1 + v2)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
