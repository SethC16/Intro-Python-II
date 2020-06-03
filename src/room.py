# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        result = f"{self.name}\n{self.description}\n"
        if self.n_to:
            result += f"N: {self.n_to.name}\n"
        if self.s_to:
            result += f"S: {self.s_to.name}\n"
        if self.e_to:
            result += f"E: {self.e_to.name}\n"
        if self.w_to:
            result += f"W: {self.w_to.name}\n"
        return result

    