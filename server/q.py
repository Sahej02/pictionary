with open("backup.txt") as infile, open("words.txt", 'w') as outfile:
    for line in infile:
        if not line.strip():
            continue
        else:
            outfile.write(line)

