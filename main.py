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

        if talent_to_add['parents'] is not None:
            for parent in talent_to_add['parents']:
                current.add_parent(talents[parent])

    test_tree = []
    for talent in talents:
        test_tree.append(pickle.dumps(talent))
    return test_tree


def find_path(tree, talents_to_spend):
    print(talents_to_spend)
    print_tree(tree)
    if talents_to_spend != 0:
        possibles = get_possible_next_talents(tree)
        print(possibles)
        for i in possibles:
            print(i)
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


def print_tree(tree_to_use):
    for e in tree_to_use:
        print(pickle.loads(e))


def claim(tree_to_use, id):
    deserialized = []
    for e in tree_to_use:
        deserialized.append(pickle.loads(e))
    deserialized[id].claim()
    return [pickle.dumps(_) for _ in deserialized]


def get_possible_next_talents(tree_to_use) -> set:
    """
    THIS IS NOT FUNCTIONAL
    :param tree_to_use:
    :return:
    """
    possible_added_talents = set()
    deserialized_tree = []
    for talent in tree_to_use:
        deserialized_tree.append(pickle.loads(talent))
    for talent in deserialized_tree:
        print(f"Testing {talent}")
        if talent.open():
            possible_added_talents.add(talent.id)
    return possible_added_talents


if __name__ == '__main__':
    tree = build_tree("druid")
    # path = find_path(tree, 30)
    print_tree(tree)
    possibles = get_possible_next_talents(tree)
    print(possibles)
    print("="*50)
    tree = claim(tree,0)
    possibles = get_possible_next_talents(tree)
    print(possibles)
