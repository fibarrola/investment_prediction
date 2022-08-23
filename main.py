from tkinter import CURRENT
import plotly.graph_objects as go

CURRENT_CAPITAL = 19200
EXP_3YR_INT = 25
FINAL_APT_VALUE = 100000

current_cash = CURRENT_CAPITAL
inv = 0
xx = list(range(12*12+2))
available_cash = [current_cash]
total_money = [current_cash+inv]
invested_money = [0]
for x in xx[:-1]:
    if x % 36 == 0:
        current_cash += (1 + EXP_3YR_INT/100)*inv
        inv = current_cash
        current_cash = 0

    current_cash += 200
    available_cash.append(current_cash)
    total_money.append(inv+current_cash)
    invested_money.append(inv)

fig = go.Figure()
fig.add_trace(go.Scatter(x=xx, y=available_cash, name='dinero disponible', mode='lines+markers'))
fig.add_trace(go.Scatter(x=xx, y=invested_money, name='dinero invertido', mode='lines+markers'))
fig.add_trace(go.Scatter(x=xx, y=total_money, name='capital total', mode='lines+markers'))
fig.show()

current_cash = 0
inv = CURRENT_CAPITAL
xx = list(range(12*12+2))
available_cash = [current_cash]
total_money = [current_cash+inv]
invested_money = [inv]
for x in xx[:-1]:
    if x == len(xx)-2:
        current_cash += FINAL_APT_VALUE
        inv = 0
    else:
        inv += 200
    available_cash.append(current_cash)
    total_money.append(inv+current_cash)
    invested_money.append(inv)

fig = go.Figure()
fig.add_trace(go.Scatter(x=xx, y=available_cash, name='dinero disponible', mode='lines+markers'))
fig.add_trace(go.Scatter(x=xx, y=invested_money, name='dinero invertido', mode='lines+markers'))
fig.add_trace(go.Scatter(x=xx, y=total_money, name='capital total', mode='lines+markers'))
fig.show()