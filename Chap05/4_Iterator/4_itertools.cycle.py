cyc = itertools.cycle(range(2,7,2))
i = 0
while i<30:
    print(next(cyc),end=';')
    i += 1

# ได้ 2;4;6;2;4;6;2;4;6;2;4;6;2;4;6;2;4;6;2;4;6;2;4;6;2;4;6;2;4;6;