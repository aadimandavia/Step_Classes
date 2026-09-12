from Rectangle import Rectangle
from Square import Square


def test_rectangle(rectangle):
    rectangle.set_width(20)
    rectangle.set_height(10)

    expected_area = 200
    actual_area = rectangle.get_area()

    print("Expected area:", expected_area)
    print("Actual area:", actual_area)


print("Testing Rectangle:")
test_rectangle(Rectangle(5, 5))

print("\nTesting Square:")
test_rectangle(Square(5, 5))