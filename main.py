from talent_info import raw_talents
from talent import Talent
import pickle
def build_tree(class_to_use):
    talents = []
    for talent_to_add in raw_talents[class_to_use]:
        talents.append(Talent(
            talent_to_add['id'],
            talent_to_add['name'],
            talent_to_add['rank_max'],
            talent_to_add['tier']
        ))
    for talent_to_add in raw_talents[class_to_use]:
        current = talents[talent_to_add['id']]
        if talent_to_add['children'] is not None:
            for child in talent_to_add['children']:
                current.add_child(talents[child])
    return talents
def find_path(tree, talents_to_spend):
    if talents_to_spend != 0:
        possibles = get_possible_next_talents(tree)
        for i in possibles:
            new_talents_to_spend = talents_to_spend - 1
            # make a list to add deserialized talents
            new_talent_list = []
            # for every serialized talent in the tree:
            for talent in tree:
                # deserialize the talent and add to the list we made.
                new_talent_list.append(pickle.loads(talent))
            # make the edit to the specific talent we need to
            new_talent_list[i].rank = new_talent_list[i].rank + 1
            # for every talent in the list:
            for talent in new_talent_list:
                # serialize the talent
                new_talent_list[talent.id] = pickle.dumps(talent)
            return find_path(new_talent_list, new_talents_to_spend)
    else:
        return tree
def get_possible_next_talents(tree) -> list:
    possible_added_talents = []
    deserialized_tree = []
    for talent in tree:
        deserialized_tree.append(pickle.loads(talent))
    for talent in deserialized_tree:
        if talent.rank == talent.rank_max:
            for child in talent.children:
                if deserialized_tree[child.id].rank < deserialized_tree[child.id].rank_max:
                    if deserialized_tree[child.id].name not in possible_added_talents:
                        possible_added_talents.append(deserialized_tree[child.id].id)
    return possible_added_talents
if __name__ == '__main__':
    tier1 = 8
    tier2 = 20
    head = build_tree("druid")
    head[0].rank = 1
    test_tree = []
    for talent in head:
        test_tree.append(pickle.dumps(talent))
    path = find_path(test_tree, 30)