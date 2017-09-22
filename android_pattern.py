graph = {
   "a":["b","d","e"],
   "b":["a","c","d","e","f"],
   "c":["b","e","f"],
   "d":["a","b","e","h","g"],
   "e":["b","a","d","g","h","i","f","c","b"],
   "f":["c","i","b","e","h"],
   "g":["d","h","e"],
   "h":["g","d","e","f","i"],
   "i":["f","e","h"]
}

import string

def find_all_paths(start_vertex,end_vertex,path=[]):
    path = path + [start_vertex]
    
    if start_vertex == end_vertex:
        return [path]
    if start_vertex not in graph:
        return []
    paths = []
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_path = find_all_paths(vertex,end_vertex,path)
            for i in extended_path:
                paths.append(i)
    return paths


def list_flattener(list_object, aux_list=[]):
    for i in list_object:
        if type(i) is not list:
            aux_list.append(i)
        else:
            list_flattener(i)
    return aux_list


def classify_path_according_to_len(list_obj, dict_obj):
    for list_item in list_obj:
        list_item = list_flattener(list_item)
        if len(list_item) in dict_obj:
            dict_obj[len(list_item)].append(list_item)
        else:
            dict_obj[len(list_item)] = [list_item]
    return dict_obj


str = string.ascii_lowercase[:9]
path_dict = {}
for s in str:
    for j in str:
        print ("finding path between {} and {}".format(s,j))
        path_dict[j] = classify_path_according_to_len(find_all_paths(s,j),{})

print(path_dict.keys())






