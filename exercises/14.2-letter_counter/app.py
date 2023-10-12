par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
par_no_space = par.lower().replace(" ", "")

for char in par_no_space:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1
print(counts)

