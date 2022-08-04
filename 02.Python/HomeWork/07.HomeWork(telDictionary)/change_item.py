def change_item_in_dict(id_were_to_change : str,what_to_change : str, new_info : str, data : dict):
    data[id_were_to_change][what_to_change] = new_info
    return data