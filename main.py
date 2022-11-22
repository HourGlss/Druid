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
    possibles = get_possible_next_talents(tree)


def get_possible_next_talents(tree) -> list:
    possible_added_talents = []
    for talent in tree:
        if talent.rank == talent.rank_max:
            for child in talent.children:
                if tree[child.id].rank < tree[child.id].rank_max:
                    if tree[child.id].name not in possible_added_talents:
                        possible_added_talents.append(tree[child.id].id)
    return possible_added_talents


if __name__ == '__main__':
    tier1 = 8
    tier2 = 20
    head = build_tree("druid")

    test_tree = build_tree("druid")
    test_tree[0].rank = 1
    test_tree[1].rank = 1
    test_tree[4].rank = 1
    test_tree[2].rank = 1
    test_tree[7].rank = 1
    print(get_possible_next_talents(test_tree))
