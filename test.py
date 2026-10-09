def point_in_quad(point, quad):
  px, py = point
  signs = []
  for i in range(4):
    x1, y1 = quad[i]
    x2, y2 = quad[(i + 1) % 4]
    cross_product = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)
    signs.append(cross_product)
  has_positive = any(s > 1e-9 for s in signs)
  has_negative = any(s < -1e-9 for s in signs)

  return not (has_positive and has_negative)

print(point_in_quad([1, 1], [[0, 0], [0, 2], [2, 2], [2, 0]]))