# rows = 6
# cols = 10
# for row in range(rows):
#     padding = row * (cols / rows)
#     for col in range(cols):
#         if col >= padding and col <= cols - padding:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

rows = 7
cols = 10
for row in range(rows):
    padding = row * (cols / rows)
    for col in range(cols):
        if (
            col >= padding and col < cols - padding or
            col <= padding and col >= cols - padding - 1
        ):
            print("* ", end="")
        else:
            print("  ", end="")
    print()
