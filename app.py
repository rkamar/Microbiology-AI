import os
from dotenv import load_dotenv
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from phi.tools.tavily import TavilyTools
from phi.llm.groq import Groq
from assistant import get_research_assistant

# Load environment variables from a .env file
load_dotenv()

# Get API keys from environment variables
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Define custom styles
app_title_style = {
    'textAlign': 'center',
    'color': '#007BFF',
    'marginTop': '20px',
    'marginBottom': '10px'
}

app_subtitle_style = {
    'textAlign': 'center',
    'color': '#6c757d',
    'marginBottom': '40px'
}

app_container_style = {
    'backgroundColor': '#f8f9fa',
    'padding': '20px',
    'borderRadius': '10px',
    'boxShadow': '0px 0px 15px rgba(0, 0, 0, 0.1)',
    'marginBottom': '20px',
    'textAlign': 'left'  # Ensure report content is left-aligned
}

button_style = {
    'width': '100%',
    'marginTop': '10px',
    'marginBottom': '10px'
}

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Microbiology AI", style=app_title_style), width=12),
    ]),
    dbc.Row([
        dbc.Col(html.H5([
            "Python code by Ristha Kamar - D131",
            html.Br(),
            "Biomedical Research Center | Qatar University"
        ], style=app_subtitle_style), width=12),
    ]),
    dbc.Row([
        dbc.Col(dcc.Markdown(id='report-output', style=app_container_style), width=12),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Input(
                id='topic-input',
                type='text',
                placeholder='Ask a long question',
                value='',
                style={'width': '100%', 'marginBottom': '20px'}
            ), width=6
        ),
    ], justify='center'),
    dbc.Row([
        dbc.Col(
            dbc.Button('Generate Report', id='generate-button', color='primary', style=button_style),
            width=6
        ),
    ], justify='center')
], style={'textAlign': 'center'})

@app.callback(
    Output('report-output', 'children'),
    Input('generate-button', 'n_clicks'),
    State('topic-input', 'value'),
    prevent_initial_call=True
)
def generate_report(n_clicks_generate, topic):
    ctx = dash.callback_context

    if not ctx.triggered:
        return ''

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'generate-button':
        model = 'llama3-70b-8192'  # Default model

        # Use TavilyTools to perform web search with API key
        tavily_tools = TavilyTools(api_key=TAVILY_API_KEY)
        tavily_search_results = tavily_tools.web_search_using_tavily(topic)
        if not tavily_search_results:
            return 'Sorry report generation failed. Please try again.'

        # Use Groq and Assistant to generate report with API key
        research_assistant = get_research_assistant(model=model, api_key=GROQ_API_KEY)
        final_report = ""

        for delta in research_assistant.run(tavily_search_results):
            final_report += delta

        return final_report

if __name__ == '__main__':
    app.run_server(debug=True)
import os
from dotenv import load_dotenv
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from phi.tools.tavily import TavilyTools
from phi.llm.groq import Groq
from assistant import get_research_assistant

# Load environment variables from a .env file
load_dotenv()

# Get API keys from environment variables
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Define custom styles
app_title_style = {
    'textAlign': 'center',
    'color': '#007BFF',
    'marginTop': '20px',
    'marginBottom': '10px'
}

app_subtitle_style = {
    'textAlign': 'center',
    'color': '#6c757d',
    'marginBottom': '40px'
}

app_container_style = {
    'backgroundColor': '#f8f9fa',
    'padding': '20px',
    'borderRadius': '10px',
    'boxShadow': '0px 0px 15px rgba(0, 0, 0, 0.1)',
    'marginBottom': '20px',
    'textAlign': 'left'  # Ensure report content is left-aligned
}

button_style = {
    'width': '100%',
    'marginTop': '10px',
    'marginBottom': '10px'
}

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Microbiology AI", style=app_title_style), width=12),
    ]),
    dbc.Row([
        dbc.Col(html.H5([
            "Python code by Ristha Kamar - D131",
            html.Br(),
            "Biomedical Research Center | Qatar University"
        ], style=app_subtitle_style), width=12),
    ]),
    dbc.Row([
        dbc.Col(dcc.Markdown(id='report-output', style=app_container_style), width=12),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Input(
                id='topic-input',
                type='text',
                placeholder='Ask a long question',
                value='',
                style={'width': '100%', 'marginBottom': '20px'}
            ), width=6
        ),
    ], justify='center'),
    dbc.Row([
        dbc.Col(
            dbc.Button('Generate Report', id='generate-button', color='primary', style=button_style),
            width=6
        ),
    ], justify='center')
], style={'textAlign': 'center'})

@app.callback(
    Output('report-output', 'children'),
    Input('generate-button', 'n_clicks'),
    State('topic-input', 'value'),
    prevent_initial_call=True
)
def generate_report(n_clicks_generate, topic):
    ctx = dash.callback_context

    if not ctx.triggered:
        return ''

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'generate-button':
        model = 'llama3-70b-8192'  # Default model

        # Use TavilyTools to perform web search with API key
        tavily_tools = TavilyTools(api_key=TAVILY_API_KEY)
        tavily_search_results = tavily_tools.web_search_using_tavily(topic)
        if not tavily_search_results:
            return 'Sorry report generation failed. Please try again.'

        # Use Groq and Assistant to generate report with API key
        research_assistant = get_research_assistant(model=model, api_key=GROQ_API_KEY)
        final_report = ""

        for delta in research_assistant.run(tavily_search_results):
            final_report += delta

        return final_report

if __name__ == '__main__':
    app.run_server(debug=True)
