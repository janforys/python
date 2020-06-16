is_female = True
is_heavy = False

if is_female and is_heavy:
    print("You are heavy female")
elif is_heavy and not is_female:
    print("You're not female but you're heavy xD")
elif not is_female and not is_heavy:
    print("You're not female and not heavy")
else:
    print("You are not heavy female")
