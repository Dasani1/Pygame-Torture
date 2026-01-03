 
level = int(input())

f = open(f"levels/{level}.txt", "w")
for _ in range(2): f.write("000000000000000000000000\n")

notes = ["cn", "cs", "dn", "ds", "en", "fn", "fs", "gn", "gs", "an", "as", "bn",
         "Cn", "Cs", "Dn", "Ds", "En", "Fn", "Fs", "Gn", "Gs", "An", "As", "Bn"]

next_notes = input()

while next_notes != "":
    beats = next_notes.split("|")
    for beat in beats:
        empty_line = ['0' for _ in range(24)] #"000000000000000000000000"

        for i in range(int(beat[0])):
            for j in range(int(len(beat)/2)):
                add = '2'
                if i == 0: 
                    add = '1'
                empty_line[notes.index(beat[1+j*2: 1+j*2+2])] = add
            string_line = ""
            for i in range(24):
                string_line = string_line + empty_line[i]
            f.write(string_line + '\n')
    next_notes = input()

f.close()
print("end")