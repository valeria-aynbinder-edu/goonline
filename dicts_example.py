# Input : test_dict = {‘Gfg’ : 4, ‘best’ : 9}, test_list = [8, 2]
# Output : {8: {‘Gfg’: 4}, 2: {‘best’: 9}}

def transform_dict(input_dict, input_list):
    ret_dict = {}

    # for list_elem in input_list:
    #
    # for dict_key in input_dict:

    for dict_key, list_elem in zip(input_dict, input_list):
        print(f"dict_key: {dict_key}, list_elem: {list_elem}")
        ret_dict[list_elem] = {dict_key: input_dict[dict_key]}



    return ret_dict


def transform_dict_no_zip(input_dict, input_list):
    ret_dict = {}

    i = 0
    for key, value in input_dict.items():
        print(f"key: {key}, val: {value}")
        ret_dict[input_list[i]] = {key: value}
        i += 1

    return ret_dict

# print(transform_dict({"Gfg" : 4, "best" : 9}, [8, 2]))

print(transform_dict_no_zip({"Gfg" : 4, "best" : 9}, [8, 2]))