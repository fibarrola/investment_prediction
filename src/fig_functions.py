import logging
import plotly.graph_objects as go


def money_graph(current_cash =0, interest = 0, return_time =12, monthly_inv =0):
    current_cash = 0 if not current_cash else current_cash
    interest = 0 if not interest else interest
    inv = 0
    xx = list(range(12*12+2))
    available_cash = [current_cash]
    total_money = [current_cash+inv]
    invested_money = [0]
    for x in xx[:-1]:
        if x % return_time == 0:
            current_cash += (1 + interest/100)*inv
            inv = current_cash
            current_cash = 0

        current_cash += monthly_inv
        available_cash.append(current_cash)
        total_money.append(inv+current_cash)
        invested_money.append(inv)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xx, y=available_cash, name='dinero disponible', mode='lines+markers'))
    fig.add_trace(go.Scatter(x=xx, y=invested_money, name='dinero invertido', mode='lines+markers'))
    fig.add_trace(go.Scatter(x=xx, y=total_money, name='capital total', mode='lines+markers'))

    return fig