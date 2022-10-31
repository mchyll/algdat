class Stack:
    elements = []
    len = 0

    def push(self, element):
        if len(self.elements) == self.len:
            self.elements.append(element)  # Utvid arrayen hvis nødvendig
        else:
            self.elements[self.len] = element
        self.len += 1

    def pop(self):
        if self.len == 0:
            return None

        self.len -= 1
        return self.elements[self.len]

    def print_stack(self):
        for i in range(self.len):
            elem = self.elements[i]
            print("{} -> ".format(elem), end='')
        print()


def check_file(filename):
    def error_msg(line, char, msg):
        print("Error on line {} position {}: {}".format(line + 1, char + 1, msg))

    stack = Stack()
    with open(filename, "r") as file:
        for linenum, line in enumerate(file):
            for charnum, char in enumerate(line):
                if char in ["{", "[", "("]:
                    stack.push(char)
                    stack.print_stack()

                elif char == "}":
                    match = stack.pop()
                    if match != "{":
                        error_msg(linenum, charnum, "unexpected }")
                        stack.push(match)
                        stack.print_stack()

                elif char == "]":
                    match = stack.pop()
                    if match != "[":
                        error_msg(linenum, charnum, "unexpected ]")
                        stack.push(match)
                        stack.print_stack()

                elif char == ")":
                    match = stack.pop()
                    if match != "(":
                        error_msg(linenum, charnum, "unexpected )")
                        stack.push(match)
                        stack.print_stack()

        rest = stack.pop()
        while rest:
            print("Error on end of file: unmatched {}".format(rest))
            rest = stack.pop()


check_file("../Oving2.java")
