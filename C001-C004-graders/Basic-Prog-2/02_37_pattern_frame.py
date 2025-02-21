def pattern_frame(s):
    n = len(s)
    top_bottom_row = "|".join(["oOoOo"] * n)
    second_fourth_row = "|".join(["O***O"] * n)
    middle_row = "|".join(["o*" + char + "*o" for char in s])
    print(top_bottom_row)
    print(second_fourth_row)
    print(middle_row)
    print(second_fourth_row)
    print(top_bottom_row)

s = input().strip()
pattern_frame(s)