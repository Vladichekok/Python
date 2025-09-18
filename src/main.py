from string_utils import print_string, check_case, smogtether_upper
from generator_utils import even_odd_generator

if __name__ == "__main__":
    print_string("Hello world")
    check_case("HELLO")
    check_case("hello")
    check_case("HelloWorld")
    print("Letter list:", smogtether_upper())

    gen = even_odd_generator()
    for _ in range(4):
        print(next(gen))
