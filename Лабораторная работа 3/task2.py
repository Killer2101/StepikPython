# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой


def find_common_participants(participants_first_group, participants_second_group, space=','):
    first_group = participants_first_group.split(space)
    second_group = participants_second_group.split(space)
    common_participants = set(first_group) & set(second_group)
    sorted_common_participants = sorted(common_participants)
    return sorted_common_participants

common_participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", common_participants)