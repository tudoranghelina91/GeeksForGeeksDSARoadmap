def generate(slist, index, output):
    if index == len(slist):
        output.append(''.join(slist))
        return
        
    if slist[index] == "?":
        slist[index] = "0"
        generate(slist, index + 1, output)
        slist[index] = "1"
        generate(slist, index + 1, output)
        slist[index] = "?"
    else:
        generate(slist, index + 1, output)

def generate_binary_string(s):
    # Code here
    output = []
    generate(list(s), 0, output)
    return output

print(generate_binary_string("10?11?1???"))
