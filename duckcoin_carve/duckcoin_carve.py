#!/usr/bin/env python3

# This is a tool used to send text files to archive them in the duckcoin blockchain.

import subprocess
import sys

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

def add_sufix_to_lines(text_cut, name):
    for i in range(len(text_cut)):
        postfix = "\n        " + name + " - " + str(i+1) + "/" + str(len(text_cut)) + "\n"
        text_cut[i] = text_cut[i] + postfix

def send_str_in_blockchain(snode_exec, txt_in, name):
    text_cut = cut_long_text(txt_in, DATA_MAX_SIZE)
    add_sufix_to_lines(text_cut, name)
    write_list(snode_exec, text_cut)

def send_file_in_blockchain(snode_exec, filename):
    f = open(filename, "r")
    test_str = f.read()
    f.close()
    send_str_in_blockchain(snode_exec, test_str, filename)

def main():
    if len(sys.argv) != 3:
        print("Usage: duckcoin_carve.py <snode binary> <file to carve>")
    else:
        send_file_in_blockchain(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

