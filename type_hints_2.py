from typing import TypedDict, NamedTuple, TypeVar, List


# An example of TypeDict
class Student(TypedDict):
    name: str
    age: int


student: Student = {
    "name": "Marcy",
    "age": 25,
}

other_student = Student(name="Jared", age=23)
print(other_student)


# An example of NamedTuple
class Point(NamedTuple):
    x: int
    y: int


point2d = Point(1, 2)
print("point2d x axis: " + str(point2d.x))
print("point2d y axis: " + str(point2d.y))

TAddableEntity = TypeVar("TAddableEntity")


def make_list_of_addable_entity(
    a: TAddableEntity, b: TAddableEntity
) -> List[TAddableEntity]:
    return [a, b]
