class Talent:
    total_talents_spent = 0
    required_for_tier1 = 8
    required_for_tier2 = 20
    children:list["Talent"]
    parents:list["Talent"]

    def __init__(self, id, name, rank_max, tier):
        self.name = name
        self.id = id
        self.children = []
        self.parents = []
        self.rank = 0
        self.rank_max = rank_max
        self.tier = tier

    def add_child(self, talent: "Talent"):
        self.children.append(talent)

    def add_parent(self, talent: "Talent"):
        self.parents.append(talent)

    def claim(self):
        self.rank += 1
        Talent.total_talents_spent += 1

    def open(self):
        if self.rank == self.rank_max:
            print("Not open because taken")
            return False
        parent_found = False
        for parent in self.parents:
            print(f"{parent.id} ({parent.rank}/{parent.rank_max})")
            if parent.rank == parent.rank_max:
                parent_found = True
                break
        if self.parents == []:
            print("starter node")
            parent_found = True
        if not parent_found:
            print("Not open because no viable parent")
            return False
        if self.tier == 2:
            if Talent.total_talents_spent >= Talent.required_for_tier2:
                return True
            else:
                print("Not open because t2 talent but not enough points")
        elif self.tier == 1:
            if Talent.total_talents_spent >= Talent.required_for_tier1:
                return True
            else:
                print("Not open because t1 talent but not enough points")
        else:
            print("OPEN")
            return True
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"p{str([e.id for e in self.parents]):<12} {self.id:>2} c{str([e.id for e in self.children])}({self.rank}/{self.rank_max})"
