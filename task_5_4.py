src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

bit_mask = (a if a > b else None for a, b in zip(src, result))

for bit_ in bit_mask:
    if bit_:  print(bit_)