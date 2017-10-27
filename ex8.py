formatter = "{} {} {} {}"

print(formatter.format("vasanth","kumar","velusamy","kalamani"))
print(formatter.format(1,2,3,4),end=" ")
lines=(
    "vasanth"
    "divi",
    "velusamy",
    "kalamani"
)

print(lines[8])

print(formatter.format(*lines))
