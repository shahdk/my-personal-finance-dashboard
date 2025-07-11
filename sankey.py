from constants import *
from sankey_income import *
from sankey_expense import *
import plotly.graph_objects as go # type: ignore


def render_sankey(option, on):
    income_amounts, income_amount_mappings = get_income_data(year=option)
    expense_amounts, expense_amount_mappings = get_expense_data(year=option)
    amounts = income_amounts + expense_amounts
    amount_mappings = dict(income_amount_mappings)
    amount_mappings.update(expense_amount_mappings)

    display_labels = [None] * len(labels)

    for i in range(len(labels)):
        label = labels[i].split("__")[1]
        amount = amount_mappings[label]
        amount_str = currency_fmt(amount)
        if on:
            display_labels[i] = labels[i].replace("__"+label+"__", amount_str)
        else:
            display_labels[i] = labels[i].replace("__"+label+"__", "")

    source_list = source.copy()
    target_list = target.copy()
    link_color_list = link_color.copy()
    node_color_list = node_color.copy()
    x_list = x.copy()
    y_list = y.copy()
    amounts_list = amounts.copy()

    for i in range(len(amounts)):
        amt = amounts[i]
        if (amt < 0):
            amounts_list[i] = amt * -1
            src = source[i]
            trgt = target[i]
            source_list[i] = trgt
            target_list[i] = src
            link_color_list[i] = red_link_color
            node_color_list[6] = red_node_color
            x_list[i] = 0.4
            y_list[i] = 0.2


    fig = go.Figure(data=[go.Sankey(
        arrangement='snap',
        node = dict(
        pad = 35,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = display_labels,
        color = node_color_list,
        x = x_list,
        y = y_list
        ),
        link = dict(
        source = source_list, # indices correspond to labels
        target = target_list,
        value = amounts_list,
        color = link_color_list
    ))])

    fig.update_layout(
        title_text="Cash Flow Sankey Diagram",
        font_size=14,
        font_family="Gravitas One"
        )
    return fig