import os

def get_field_args_dict(field, duplicage_args_counts, all_args_dict=None):
    if all_args_dict is None:
        all_args_dict = {}
    field_args_dict = {}

    for argument in field.arguments:
        if argument.name in duplicage_args_counts:
            index = duplicage_args_counts[argument.name] + 1
            duplicage_args_counts[argument.name] = index
            field_args_dict["{}{}".format(
                argument.name,
                index
            )] = argument
        elif argument.name in all_args_dict:
            duplicage_args_counts[argument.name] = 1
            field_args_dict["{}1".format(argument.name)] = argument
        else:
            field_args_dict[argument.name] = argument
    return field_args_dict


def get_args_to_vars_str(dict):
    list = []
    for var_name, argument in dict.items():
        list.append(
            "{}: ${}".format(
                argument.name,
                var_name
            )
        )
    return ", ".join(list)


def get_vars_to_types_str(dict):
    list = []
    for var_name, argument in dict.items():
        list.append(
            "${}: {}".format(
                var_name,
                argument.type
            )
        )
    return ", ".join(list)

def mkdir_if_not_exist(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            raise Exception("mkdir failed: {}".format(path))