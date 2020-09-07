import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import random

pd.options.mode.chained_assignment = None

df1 = pd.read_csv("shootings.csv")

df = df1[["name", "date", 'manner_of_death', 'age', 'gender', 'race', 'city', 'state', 'signs_of_mental_illness']]

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df['date'] = pd.to_datetime(df['date'])

df['age'] = df['age'].astype(int)

year_2016 = df[df['date'].dt.year == 2016]


def all_years_data():
    years_listed = df['date'].dt.year.unique()
    dict_data = {}
    for i in years_listed:
        dict_data[i] = df[df['date'].dt.year == i]
    return dict_data


dict_data = all_years_data()


def graph1_dash(dict_data):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = html.Div(children=[
        html.H1(children='Statistics on US shootings in years 2015-2020'),

        html.Div(children='''
             Source of data : https://www.kaggle.com/mrmorj/data-police-shootings
        ''', style={'margin-left': '50px'}),

        dcc.Graph(
            id='graph',
        ),
        html.Div([
            dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'Deaths of particular races in given year', 'value': 'fig_1'},
                    {'label': 'Deaths of particular races in given state', 'value': 'fig_2'},
                    {'label': 'Average age of death due to shootings', 'value': 'fig_3'},
                    {'label': 'Deaths in cities', 'value': 'fig_4'},
                    {'label': 'Deaths by months', 'value': 'fig_5'},
                ],
                value='fig_1',
                style={'width': '50%', 'margin-left': '50px'},
                clearable=False
            ),
            html.Br(), html.Br(),
            dcc.Slider(
                id='year-slider',
                min=2015,
                max=2020,
                step=1,
                value=2015,
                marks={
                    2015: {'label': '2015'},
                    2016: {'label': '2016'},
                    2017: {'label': '2017'},
                    2018: {'label': '2018'},
                    2019: {'label': '2019'},
                    2020: {'label': '2020'},
                },
            ),
        ]),

    ])

    @app.callback(
        dash.dependencies.Output('graph', 'figure'),
        [dash.dependencies.Input('year-slider', 'value'),
         dash.dependencies.Input('demo-dropdown', 'value')])
    def update_figure(year, value):
        selected_y = dict_data.get(year)
        race_this_year = selected_y.groupby(["race"]).size()
        race_in_state = selected_y.groupby(["state", "race"]).size()
        average_age = selected_y.groupby("state")['age'].mean()
        cities = selected_y.groupby(['city']).size()
        selected_y['month'] = selected_y['date'].dt.month
        months = selected_y.groupby(['month']).size()

        df_1 = pd.DataFrame({
            "Race": list(race_this_year.index),
            "Deaths": race_this_year.values
        })

        fig_1 = px.bar(df_1, x="Race", y="Deaths", color="Race", title="Deaths of particular races in given year")

        df_2 = pd.DataFrame({
            "State": race_in_state.index.get_level_values(0),
            "Race": race_in_state.index.get_level_values(1),
            "Deaths": race_in_state.values,
        })

        fig_2 = px.bar(df_2, x="State", y="Deaths", color="Race", barmode='group',
                       title="Deaths of particular races in given state",
                       color_discrete_sequence=["purple", "blue", "green", "red", "cyan", "orange"],
                       category_orders={"Race": ["Native", "Asian", "Hispanic", "Black", "White", "Other"]})

        df_3 = pd.DataFrame({
            "State": list(average_age.index),
            "Age": average_age.values,
        })

        fig_3 = px.bar(df_3, x="State", y="Age", color="Age", barmode='group',
                       title="Average age of death due to shootings")

        df_4 = pd.DataFrame({
            "City": cities.index,
            "Deaths": cities.values,
            "Position_X": [random.randint(1, 200) for x in range(len(cities))],
            "Position_Y": [random.randint(1, 100) for y in range(len(cities))],
        })

        fig_4 = px.scatter(df_4, x="Position_X", y="Position_Y", size="Deaths", color="Deaths", size_max=15,
                           title="Deaths in cities", hover_name="City",
                           hover_data={"Position_X": False, "Position_Y": False})

        df_5 = pd.DataFrame({
            "Month": list(months.index),
            "Deaths": months.values,
        })

        fig_5 = px.bar(df_5, x="Month", y="Deaths", color="Deaths",
                       title="Deaths by months")

        if value == 'fig_1':
            return fig_1
        elif value == 'fig_2':
            return fig_2
        elif value == 'fig_3':
            return fig_3
        elif value == 'fig_4':
            return fig_4
        else:
            return fig_5

    app.run_server(debug=True)


graph1_dash(dict_data)
