import tkinter as tk
import math
import random
import sympy

master = tk.Tk()
master.title("RSA assignment")
master.geometry("700x880")

def encode():
    str01 = entry_str.get()

    rows = math.ceil(len(str01) / 7)
    arr = [["0" for i in range(7)] for j in range(rows)]

    l = 0

    # convert the string into the created 2d array
    for i in range(len(arr)):
        for j in range(7):
            if l < len(str01):
                arr[i][j] = str01[l]
                l += 1
            else:
                arr[i][j] = " "

    # convert the characters into int equivalent
    for i in range(len(arr)):
        for j in range(7):
            arr[i][j] = ord(arr[i][j])

    lbl_int01.config(text=f"{arr}")

    # convert the int to binary
    for i in range(len(arr)):
        for j in range(7):
            arr[i][j] = format(arr[i][j], "b")

    lbl_bin01.config(text=f"{arr}")

    # create a new array to contain the joined binary and then it will be changed to decimal part
    temp02 = ["" for i in range(rows)]

    # binary => long binary => decimal
    for i in range(len(arr)):
        for j in range(7):
            temp01 = ["0" for i in range(10)]
            for k in range(len(arr[i][j])):
                temp01[len(temp01) - 1 - k] = arr[i][j][-1 * (k + 1)]
            temp_str = "".join(temp01)
            temp02[i] += temp_str
        temp02[i] = int(temp02[i], 2)

    lbl_dcml01.config(text = f"{temp02}")

    p = 0
    q = 0

    # generate the p and q
    while p == q:
        p = sympy.randprime(1000000000000000, 9999999999999999)
        q = sympy.randprime(1000000000000000, 9999999999999999)

    # generate the n
    n = p * q

    lbl_n.config(text = f" n : {n}")

    # generate the phi(n)
    pn = (p - 1) * (q - 1)

    # generate the e
    while True:
        e = random.randint(1, pn)
        result = math.gcd(e, pn)
        if result == 1:
            break

    lbl_e.config(text = f" e : {e}")

    # generate the d
    d = pow(e, -1, pn)

    lbl_d.config(text = f" d : {d}")

    ct = ["" for i in range(rows)]

    # convert the decimal part to cipher text
    for i in range(len(temp02)):
        ct[i] = pow(temp02[i], e, n)

    lbl_enc01.config(text = f"{ct}")

    ot = ["" for i in range(rows)]

    final_string = ""

    # convert the cipher text to original text (long binary)
    for i in range(len(temp02)):
        ot[i] = pow(ct[i], d, n)
        ot[i] = format(ot[i], "b")

    # add any missing 0 s to the would be beginning (left side) of the long binary
    for i in range(len(ot)):
        ot[i] = ((70 - len(ot[i])) * "0") + ot[i]

    lbl_Lbin01.config(text = f"{ot}")

    # convert the long binary into pieces and concatenate the char results
    for i in range(len(ot)):
        temp03 = ["" for i in range(7)]

        for j in range(len(ot[i])):
            if j < 10:
                temp03[0] += ot[i][j]
            if j >= 10 and j < 20:
                temp03[1] += ot[i][j]
            if j >= 20 and j < 30:
                temp03[2] += ot[i][j]
            if j >= 30 and j < 40:
                temp03[3] += ot[i][j]
            if j >= 40 and j < 50:
                temp03[4] += ot[i][j]
            if j >= 50 and j < 60:
                temp03[5] += ot[i][j]
            if j >= 60 and j < 70:
                temp03[6] += ot[i][j]

        # convert the binary to int then to char
        for k in range(len(temp03)):
            temp03[k] = int(temp03[k], 2)
            temp03[k] = chr(temp03[k])

        # concatenate the char results in temp03
        final_string += "".join(temp03)

    lbl_fin01.config(text = f"{final_string}")


btn_encode = tk.Button(master, text = "Do It", command = encode)
entry_str = tk.Entry(master, width = 100)

lbl_int = tk.Label(master, text = "text (int) block")
lbl_int01 = tk.Label(master, text = " ", bd = 4, bg="white", height = 3, wraplengt=500, width = 80)

lbl_bin = tk.Label(master, text = "text binary block")
lbl_bin01 = tk.Label(master, text = " ", bd = 4, bg="white", height = 8, wraplengt=500, width = 80)

lbl_dcml = tk.Label(master, text = "text decimal part")
lbl_dcml01 = tk.Label(master, text = " ", bd = 4, bg="white", height = 3, wraplengt=500, width = 80)

lbl_n = tk.Label(master, text = " n ")
lbl_n01 = tk.Label(master, text = " ")
lbl_d = tk.Label(master, text = " d ")
lbl_d01 = tk.Label(master, text = " ")
lbl_e = tk.Label(master, text = " e ")
lbl_e01 = tk.Label(master, text = " ")

lbl_enc = tk.Label(master, text = "text encryption")
lbl_enc01 = tk.Label(master, text = " ", bd = 4, bg="white", height = 3, wraplengt=500, width = 80)

lbl_Lbin = tk.Label(master, text = "text long binary")
lbl_Lbin01 = tk.Label(master, text = " ", bd = 4, bg="white", height = 8, wraplengt=600, width = 80)

lbl_fin = tk.Label(master, text = "final result")
lbl_fin01 = tk.Label(master, text = " ", bd = 4, bg="white", height = 2)

#scrollbar = tk.Scrollbar(master, orient="vertical")

entry_str.grid(row=0, column = 0, padx = 10, pady = 10)
btn_encode.grid(row=1, column = 0, padx = 10, pady = 4)

lbl_int.grid(row=2, column = 0, padx = 10, pady = 4)
lbl_int01.grid(row=3, column = 0, padx = 10, pady = 4)

lbl_bin.grid(row=4, column = 0, padx = 10, pady = 4)
lbl_bin01.grid(row=5, column = 0, padx = 10, pady = 4)

lbl_dcml.grid(row=6, column = 0, padx = 10, pady = 4)
lbl_dcml01.grid(row=7, column = 0, padx = 10, pady = 4)

lbl_n.grid(row=8, column = 0, padx = 10, pady = 4)
#lbl_n01.grid(row=9, column = 1, padx = 10, pady = 10)

lbl_d.grid(row=10, column = 0, padx = 10, pady = 4)
#lbl_d01.grid(row=11, column = 1, padx = 10, pady = 10)

lbl_e.grid(row=12, column = 0, padx = 10, pady = 4)
#lbl_e01.grid(row=13, column = 1, padx = 10, pady = 10)

lbl_enc.grid(row=14, column = 0, padx = 10, pady = 4)
lbl_enc01.grid(row=15, column = 0, padx = 10, pady = 4)

lbl_Lbin.grid(row=16, column = 0, padx = 10, pady = 4)
lbl_Lbin01.grid(row=17, column = 0, padx = 10, pady = 4)

lbl_fin.grid(row=18, column = 0, padx = 10, pady = 4)
lbl_fin01.grid(row=19, column = 0, padx = 10, pady = 4)


#scrollbar.grid(row = 0, rowspan = 12 , column = 2, sticky = "ns")

master.mainloop()