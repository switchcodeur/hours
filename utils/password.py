from secrets import choice as rchoice

characters = [chr(i) for i in range(33, 127)]
def generate(length: int) -> str:
    return "".join([rchoice(characters) for i in range(length)])