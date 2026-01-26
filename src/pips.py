from enum import Enum, unique


@unique
class Pips(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @classmethod
    def values(cls):
        return [number._value_ for number in Pips.__members__.values()]

    @classmethod
    def reversedValues(cls):
        return reversed(cls.values())

    @classmethod
    def minus(cls, pip):
        return set(cls.values()) - {pip.value}



class Combinations(Enum):
    ALL_THE_SAME = 1
    PAIR = 2
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FOUR_OF_A_KIND = 4
    FULL_HOUSE_DIFERENT_VALUES = 2
    


if __name__ == "__main__":
    from colorama import Fore
    print(Fore.YELLOW + "Lista de 'clave-valor'" + Fore.RESET)
    print(list(Pips))

    print(Fore.YELLOW + "Formas de obtener el atributo de la clase" + Fore.RESET)
    print(Fore.YELLOW + "Por valor" + Fore.RESET)
    print(Pips(1))

    print(Fore.YELLOW + "Por nombre" + Fore.RESET)
    print(Pips["ONE"])

    print(Fore.YELLOW + "Por atributo" + Fore.RESET)
    print(Pips.ONE)

    print(Fore.YELLOW + "Devuelve el nobre de la constante en la clase" + Fore.RESET)
    print(Pips.ONE.name)

    print(Fore.YELLOW + "Devuelve el valor de la constante en la clase" + Fore.RESET)
    print(Pips.ONE.value)

    print(Fore.YELLOW + "Itera sobre los miembros de la clase y devuelve sus valores" + Fore.RESET)
    for number in Pips.__members__.values():
        print(number._value_)

    print(Fore.YELLOW + "Llama las funciones de la clase" + Fore.RESET)
    print(Pips.values())
    print(list(Pips.reversedValues()))
    print(Pips.minus(Pips.FIVE))