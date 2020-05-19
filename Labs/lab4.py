import random
import Tkinter as tk

n = 11
m = 11
p = 0.5927
sum = 0
r = [[0 for x in range(m)] for x in range(n)]
s = [[0 for x in range(m)] for x in range(n)]
x = [0 for x in range(m)]
y = [0 for x in range(m)]
for i in range(0, n):
    for j in range(0, m):
        r[i][j] = random.random()
x0 = 10
y0 = 10
dx = 20
dy = 20
x1 = 30
y1 = 30
root = tk.Tk()
canvas = tk.Canvas(root)
canvas["width"] = 600
canvas["height"] = 400
canvas.pack()
for i in range(0, n):
    for j in range(0, m):
        if r[i][j] < p:
            s[i][j] = 1
            square = canvas.create_rectangle(x0, y0, x1, y1, fill="green")
            text = canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text="1", font=("Arial", "8"))
        else:
            s[i][j] = 0
            square = canvas.create_rectangle(x0, y0, x1, y1, fill='white')
            text = canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text="0", font=("Arial", "8"))
        y0 += dy
        y1 += dy
    y0 = 10
    y1 = 30
    x0 += dy
    x1 += dy
print('\nr {0}'.format(r))
print('\ns {0}'.format(s))
for i in range(0, n):
    for j in range(0, m):
        sum = sum + s[i][j]
sum1 = float(sum)
number = float(n * m)
percol = sum1 / number
print('summ = %s percolation=%.2f' % (sum1, percol))
root.mainloop()
