from talent_info import raw_talents
from talent import Talent
import pickle


def build_tree(class_to_use):
    talents = []
    for talent_to_add in raw_talents[class_to_use]:
        talents.append(Talent(
            talent_to_add['id'],
            talent_to_add['name'],
            0,
            talent_to_add['rank_max'],
            talent_to_add['tier']
        ))
    add_children_and_parents(talents, class_to_use)
    return talents


def add_children_and_parents(talents, class_to_use):
    for talent_to_add in raw_talents[class_to_use]:
        current = talents[talent_to_add['id']]

        if talent_to_add['children'] is not None:
            for child in talent_to_add['children']:
                current.add_child(talents[child])

        if talent_to_add['parents'] is not None:
            for parent in talent_to_add['parents']:
                current.add_parent(talents[parent])


def find_path(class_to_use, tree_to_use, talents_to_spend):
    if talents_to_spend != 0:
        possibles = get_possible_next_talents(tree_to_use)
        for i in possibles:
            new_talents_to_spend = talents_to_spend - 1
            new_talent_list = []
            for talent in tree_to_use:
                new_talent_list.append(talent.copy())
            add_children_and_parents(new_talent_list, class_to_use)
            new_tree = claim(new_talent_list, i)
            return find_path(class_to_use, new_tree, new_talents_to_spend)
    else:
        print_tree(tree_to_use)
        return


def print_tree(tree_to_use):
    for e in tree_to_use:
        print(e)


def claim(tree_to_use, ids):
    if isinstance(ids, int):
        tree_to_use[ids].claim()
        print(f"claiming {tree_to_use[ids].name}")
    if isinstance(ids, list):
        for x in ids:
            tree_to_use[x].claim()
    return tree_to_use


def get_possible_next_talents(tree_to_use) -> set:
    possible_added_talents = set()
    for talent in tree_to_use:
        if talent.open():
            possible_added_talents.add(talent.id)
    return possible_added_talents


if __name__ == '__main__':
    tree = build_tree("druid")
    # tree = claim(tree, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 21, 23, 23, 24])
    # possibles = get_possible_next_talents(tree)
    # print(possibles)
    find_path("druid", tree, 8)
