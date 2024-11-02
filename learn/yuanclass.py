def create(pos=None):
    if pos is None:
        pos = [0, 0]

    def go(direction, step):
        new_x = pos[0] + direction[0] * step
        new_y = pos[1] + direction[1] * step

        pos[0] = new_x
        pos[1] = new_y

        return pos

    return go


player = create()
print(player([1, 0], 10))
print(player([0, 1], 20))
print(player([-1, 0], 10))
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side * self.side
#
# def shape_factory(shape_type, **kwargs):
#     if shape_type == 'circle':
#         return Circle(kwargs.get('radius', 1))
#     elif shape_type == 'square':
#         return Square(kwargs.get('side', 1))
#     else:
#         raise ValueError("Unknown shape type")
#
# # 使用工厂函数创建对象
# circle = shape_factory('circle', radius=5)
# print(f"Circle Area: {circle.area()}")  # 输出: Circle Area: 78.5
#
# square = shape_factory('square', side=4)
# print(f"Square Area: {square.area()}")  # 输出: Square Area: 16