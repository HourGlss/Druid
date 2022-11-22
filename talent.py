class Talent:
    def __init__(self, id, name, rank_max, tier):
        self.name = name
        self.id = id
        self.children = []
        self.rank = 0
        self.rank_max = rank_max
        self.tier = tier

    def add_child(self, talent: "Talent"):
        self.children.append(talent)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.id}\t{str(self.name):<50} ({self.rank}/{self.rank_max})"
