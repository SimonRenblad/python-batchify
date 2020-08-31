# made by Simon Renblad

# Converts list into batched_list
def batchify(target_list, batch_size):

    result_list = []

    num_elems = len(target_list)

    num_batches = num_elems / batch_size

    batch_i = 0

    # create batches of length = batch_size
    while batch_i < num_batches:
        result_list.append(target_list[(batch_i * batch_size):((batch_i + 1) * batch_size)])
        batch_i += 1

    return result_list

# converts batched_list into list
def unbatchify(target_list):

    result_list = []

    for batch in target_list:
        result_list += batch

    return result_list

# boolean function to see whether list is batched_list
def is_batched(target_list):

    if not isinstance(target_list[0], list):
        return False

    batch_size = len(target_list[0])
    num_uniform_batch = len(target_list) - 1

    batch_i = 1
    while batch_i < num_uniform_batch:
        if not isinstance(target_list[batch_i], list):
            return False
        if len(target_list[batch_i]) != batch_size:
            return False

        batch_i += 1

    if not isinstance(target_list[num_uniform_batch], list):
        return False

    if len(target_list[num_uniform_batch]) > batch_size:
        return False

    return True
