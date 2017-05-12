
__auth__ = "Caspar"

import types

class Age:
    zero = 0
    six = 6
    Seventeen = 17
    fouty = 40
    sixty_five = 65
    sixty_six = 66

def get_age_group_with_age(age):
    if type(age) is not types.IntType:
        return "The age must be an int number"
    if age < Age.zero:
        return "You are not born yet"
    isBaby = age <= Age.six
    if isBaby:
        return "You are baby"
    isJuvenile = age <= Age.Seventeen
    if isJuvenile:
        return "You are juvenile"
    isYouth = age <= Age.fouty
    if isYouth:
        return "You are youth"
    isMidlife = age <= Age.sixty_five
    if isMidlife:
        return "You are mid life"
    isOldAge = age >= Age.sixty_six
    if isOldAge:
        return "You are old age"

def main():
    age = 1.0
    print(get_age_group_with_age(age))

if __name__ == '__main__':
    main()
