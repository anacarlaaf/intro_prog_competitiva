n = int(input())
m = int(input())

reps_completas = n // m
sobra = n - reps_completas

if sobra == 0:
    # inicia novo set
    if reps_completas % 2 == 0:
        print("MARCEL")
    else:
        print("JOAOZAO")
else:
    # continua set
    if reps_completas % 2 == 0:
        print("MARCEL")
    else:
        print("JOAOZAO")
