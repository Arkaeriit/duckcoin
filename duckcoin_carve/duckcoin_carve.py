#!/usr/bin/env python3

import subprocess

DATA_MAX_SIZE = 50 * 1024

# This function write each string in the lst argument to the duckcoin blockchain
def write_list(snode_exec, lst):
    for element in(lst):
        subprocess.run([snode_exec, "1", "--data", element])

#write_list("../snode-src/duckcoin", ["elem1", "elem2", "elem3"])

def cut_long_text(txt_in, max_size):
    ret = []
    old_pointer = 0
    pointer = max_size
    while old_pointer != len(txt_in):
        if pointer >= len(txt_in):
            ret.append(txt_in[old_pointer:len(txt_in)])
            return ret
        while txt_in[pointer] != " " or txt_in[pointer] != "\n":
            if pointer <= old_pointer:
                pointer = old_pointer + max_size
                break
            pointer -= 1
        ret.append(txt_in[old_pointer:pointer])
        old_pointer = pointer
        pointer = old_pointer + max_size
    return ret

#print(cut_long_text("La dqzdsejh  hje jhse fjh jh djq djqz djhqz djhqz djhqz dqzjh djqzh dqzjd jqzhd qzjd qzjh dqzdqzid qzd qzd qzdqz dqz d qzd qzd zdzdqdqzfrftg trrssfefrg gtnuehfyusryfseydusefys fef fseyfstbtvfsvefysensueinidqendi euiqdnuiqendiuqndiqneindiqeni",10))

def send_str_in_blockchain(snode_exec, txt_in):
    write_list(snode_exec, cut_long_text(txt_in, DATA_MAX_SIZE))

f = open("test.txt", "r")
test_str = f.read()
f.close()
send_str_in_blockchain("../snode-src/duckcoin", test_str)

