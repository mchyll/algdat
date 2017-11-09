class Automat:

    def __init__(self, input_alphabet, accept_states, next_states):
        self.input_alphabet = input_alphabet
        self.accept_states = accept_states
        self.next_states = next_states
        self.current_state = 0

    def sjekk_input(self, input):
        self.current_state = 0

        for char in input:
            char_index = self.input_alphabet.index(char)
            self.current_state = self.next_states[self.current_state][char_index]

        return self.current_state in self.accept_states


if __name__ == "__main__":
    a = Automat(
        ["0", "1"],
        [2],
        [
            [1, 3],
            [1, 2],
            [2, 3],
            [3, 3]
        ]
    )

    print(a.sjekk_input(""))
    print(a.sjekk_input("010"))
    print(a.sjekk_input("111"))
    print(a.sjekk_input("010110"))
    print(a.sjekk_input("001000"))
    print()

    b = Automat(
        ["a", "b"],
        [3],
        [
            [1, 2],
            [4, 3],
            [3, 4],
            [3, 3],
            [4, 4],
        ]
    )

    print(b.sjekk_input("abbb"))
    print(b.sjekk_input("aaab"))
    print(b.sjekk_input("babab"))
