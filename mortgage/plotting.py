from typing import List
import plotly.graph_objects as go


def plot_overview(
        years: List[int], remaining_principal: List[float], interest_paid_term: List[float],
        monthly_payment: float):
    trace1 = go.Bar(
        x=years,
        y=remaining_principal,
        name='Remaining Principal',
        yaxis='y1'
    )
    trace2 = go.Bar(
        x=years,
        y=interest_paid_term,
        name='Interest Paid Term',
        yaxis='y1'
    )
    trace3 = go.Scatter(
        x=years,
        y=[monthly_payment] * len(years),
        name='Monthly Payment',
        mode='lines',
        yaxis='y2',
        line=dict(color="#000000")
    )

    data = [trace1, trace2, trace3]
    layout = go.Layout(title='Mortgage Overview',
                       yaxis=dict(title='Principal'),
                       yaxis2=dict(title='Interest',
                                   overlaying='y',
                                   side='right'))

    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(
        dict(
            title=dict(
                text='<b>Mortgage Overview</b>',
                x=0.5,
                xanchor='center',
                yanchor='top',
                font= {'size': 20}
                )
        )
    )
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
        )
    )

    return fig
