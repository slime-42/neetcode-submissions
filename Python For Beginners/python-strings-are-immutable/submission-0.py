def remove_fourth_character(word: str) -> str:

    x = word[4]

    s1 = word[:3]
    s2 = word[4:]

    new_string = s1+s2

    return(new_string)

    pass


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
