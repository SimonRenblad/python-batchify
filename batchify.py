# made by Simon Renblad

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
