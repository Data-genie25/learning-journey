import random

heads = 0
tails = 0

for i in range(10):
    flip = random.choice(["heads", "tails"])
    print(f"Flip {i + 1}: {flip}")
    if flip == "heads":
        heads = heads + 1
    else:
        tails = tails + 1

print(f"\nFinal score: Heads {heads}, Tails {tails}")