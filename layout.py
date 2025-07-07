import dash_bootstrap_components as dbc
from dash import dcc, html

# Sidebar layout
sidebar = html.Div(
    [
        html.Div(
            [
                html.Img(src='/assets/logo.webp', style={'width': '100%', 'height': 'auto'}),
                html.Hr(),
                dbc.NavLink([html.I(className="fas fa-home"), " Home"], href="/", style={'fontSize': '16px', 'fontWeight': 'bold'}),
                html.Hr(),
                dbc.Button(
                    [html.I(className="fas fa-database"), " Datasets"], id="datasets-button", className="mb-2", n_clicks=0,
                    style={'fontSize': '16px', 'fontWeight': 'bold', 'backgroundColor': 'transparent', 'border': 'none', 'color': 'green'}
                ),
                dbc.Collapse(
                    html.Div(
                        [
                            html.H2("European Space Agency (ESA)", className="display-0", style={'fontSize': '18px'}),
                            dbc.Button(
                                [html.I(className="fas fa-globe"), " GlobColour"], id="globcolor-button", className="mb-2", n_clicks=0,
                                style={'fontSize': '16px'}
                            ),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavLink([html.I(className="fas fa-sun"), " Reflectance"], href="/esa/globcolor/reflectance", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-water"), " PP"], href="/esa/globcolor/pp", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-eye"), " Optics"], href="/esa/globcolor/optics", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-tint"), " Transp"], href="/esa/globcolor/transp", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-fish"), " Plankton"], href="/esa/globcolor/plankton", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                    ], vertical=True
                                ),
                                id="globcolor-collapse",
                                is_open=True,
                            ),
                            dbc.Button(
                                [html.I(className="fas fa-satellite"), " Sentinel"], id="sentinel-button", className="mb-2", n_clicks=0,
                                style={'fontSize': '16px'}
                            ),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavLink([html.I(className="fas fa-leaf"), " Chl-a"], href="/esa/sentinel/olci", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                    ], vertical=True
                                ),
                                id="sentinel-collapse",
                                is_open=True,
                            ),
                            html.Hr(),
                            html.H2("UK Met Office (UKMO)", className="display-6", style={'fontSize': '18px'}),
                            dbc.NavLink([html.I(className="fas fa-cloud"), " SST"], href="/ukmo/ostia", style={'fontSize': '14px'}),
                            html.Hr(),
                            html.H2("NASA", className="display-6", style={'fontSize': '18px'}),
                            dbc.Button(
                                [html.I(className="fas fa-thermometer-half"), " GHRSST"], id="ghrsst-button", className="mb-2", n_clicks=0,
                                style={'fontSize': '16px'}
                            ),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavLink([html.I(className="fas fa-map"), " SST"], href="/nasa/ghrsst/mur", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                    ], vertical=True
                                ),
                                id="ghrsst-collapse",
                                is_open=True,
                            ),
                            dbc.Button(
                                [html.I(className="fas fa-satellite-dish"), " MODIS"], id="modis-button", className="mb-2", n_clicks=0,
                                style={'fontSize': '16px'}
                            ),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavLink([html.I(className="fas fa-leaf"), " POC"], href="/nasa/modis/poc", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-cube"), " PIC"], href="/nasa/modis/pic", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-lightbulb"), " PAR"], href="/nasa/modis/par", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                    ], vertical=True
                                ),
                                id="modis-collapse",
                                is_open=True,
                            ),
                            html.Hr(),
                            html.H2("Mercator Ocean International (MOI)", className="display-6", style={'fontSize': '18px'}),
                            dbc.Button(
                                [html.I(className="fas fa-cogs"), " MODEL"], id="model-button", className="mb-2", n_clicks=0,
                                style={'fontSize': '16px'}
                            ),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavLink([html.I(className="fas fa-fish"), html.B(" PISCES")], href="#", id="pisces-link", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.Collapse(
                                            dbc.Nav(
                                                [
                                                    dbc.NavLink([html.I(className="fas fa-dna"), " Bio"], href="/moi/model/pisces/bio", style={'fontSize': '14px', 'paddingLeft': '40px'}),
                                                    dbc.NavLink([html.I(className="fas fa-apple-alt"), " Nut"], href="/moi/model/pisces/nut", style={'fontSize': '14px', 'paddingLeft': '40px'}),
                                                    dbc.NavLink([html.I(className="fas fa-eye"), " Optics"], href="/moi/model/pisces/optics", style={'fontSize': '14px', 'paddingLeft': '40px'}),
                                                    dbc.NavLink([html.I(className="fas fa-leaf"), " Car"], href="/moi/model/pisces/car", style={'fontSize': '14px', 'paddingLeft': '40px'}),
                                                    dbc.NavLink([html.I(className="fas fa-cube"), " CO₂"], href="/moi/model/pisces/co2", style={'fontSize': '14px', 'paddingLeft': '40px'}),
                                                    dbc.NavLink([html.I(className="fas fa-seedling"), " PFTs"], href="/moi/model/pisces/pfts", style={'fontSize': '14px', 'paddingLeft': '40px'})
                                                ], vertical=True
                                            ),
                                            id="pisces-collapse",
                                            is_open=True,
                                        ),
                                        dbc.NavLink([html.I(className="fas fa-fish"), html.B(" SEAPODYM")], href="#", id="seapodym-link", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.Collapse(
                                            dbc.Nav(
                                                [
                                                    dbc.NavLink([html.I(className="fas fa-weight"), " Biomass"], href="/moi/model/seapodym/biomass", style={'fontSize': '14px', 'paddingLeft': '40px'})
                                                ], vertical=True
                                            ),
                                            id="seapodym-collapse",
                                            is_open=True,
                                        ),
                                        dbc.NavLink([html.I(className="fas fa-water"), html.B(" NEMO")], href="#", id="nemo-link", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.Collapse(
                                            dbc.Nav(
                                                [
                                                    dbc.NavLink([html.I(className="fas fa-tint"), " Salinity"], href="/moi/model/nemo/salinity", style={'fontSize': '14px', 'paddingLeft': '40px'})
                                                ], vertical=True
                                            ),
                                            id="nemo-collapse",
                                            is_open=True,
                                        ),
                                    ], vertical=True
                                ),
                                id="model-collapse",
                                is_open=True,
                            ),
                        ]
                    ),
                    id="datasets-collapse",
                    is_open=False,
                ),
            ],
            id="sidebar-content",
            style={"display": "block"}
        ),
    ],
    id="sidebar",
    className="sidebar d-none d-md-block",  # Hide on mobile, show on desktop
    style={
        "width": "280px",
        "height": "100vh",
        "position": "fixed",
        "top": 0,
        "left": 0,
        "z-index": 1000,
        "overflow-y": "auto",
        "padding": "1.5rem",
        "background": "linear-gradient(180deg, #111827 0%, #374151 100%)",
        "color": "#e5e7eb",
        "box-shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1)",
        "border-right": "1px solid #d1d5db"
    }
)

# Mobile sidebar (offcanvas for mobile devices)
mobile_sidebar = dbc.Offcanvas(
    [
        html.Div(
            [
                html.Img(src='/assets/logo.webp', style={'width': '100%', 'height': 'auto', 'marginBottom': '1rem'}),
                html.Hr(style={'borderColor': 'rgba(255, 255, 255, 0.1)'}),
                dbc.NavLink([html.I(className="fas fa-home"), " Home"], href="/", 
                           style={'fontSize': '16px', 'fontWeight': 'bold', 'color': '#e5e7eb', 'textDecoration': 'none'}),
                html.Hr(style={'borderColor': 'rgba(255, 255, 255, 0.1)'}),
                html.Button(
                    [html.I(className="fas fa-database"), " Datasets"], 
                    id="mobile-datasets-button", 
                    className="btn", 
                    n_clicks=0,
                    style={
                        'fontSize': '16px', 
                        'fontWeight': 'bold', 
                        'backgroundColor': 'transparent', 
                        'border': '1px solid rgba(255, 255, 255, 0.2)', 
                        'color': '#e5e7eb',
                        'width': '100%',
                        'textAlign': 'left',
                        'padding': '0.75rem 1rem',
                        'borderRadius': '0.75rem',
                        'margin': '0.25rem 0'
                    }
                ),
                dbc.Collapse(
                    html.Div(
                        [
                            html.H2("European Space Agency (ESA)", className="display-0", style={'fontSize': '18px'}),
                            html.Button(
                                [html.I(className="fas fa-globe"), " GlobColour"], 
                                id="mobile-globcolor-button", 
                                className="btn", 
                                n_clicks=0,
                                style={
                                    'fontSize': '16px',
                                    'backgroundColor': 'transparent', 
                                    'border': '1px solid rgba(255, 255, 255, 0.2)', 
                                    'color': '#e5e7eb',
                                    'width': '100%',
                                    'textAlign': 'left',
                                    'padding': '0.75rem 1rem',
                                    'borderRadius': '0.75rem',
                                    'margin': '0.25rem 0'
                                }
                            ),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavLink([html.I(className="fas fa-sun"), " Reflectance"], href="/esa/globcolor/reflectance", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-water"), " PP"], href="/esa/globcolor/pp", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-eye"), " Optics"], href="/esa/globcolor/optics", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-tint"), " Transp"], href="/esa/globcolor/transp", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-fish"), " Plankton"], href="/esa/globcolor/plankton", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                    ], vertical=True
                                ),
                                id="mobile-globcolor-collapse",
                                is_open=False,
                            ),
                            html.Button(
                                [html.I(className="fas fa-satellite"), " Sentinel"], 
                                id="mobile-sentinel-button", 
                                className="btn", 
                                n_clicks=0,
                                style={
                                    'fontSize': '16px',
                                    'backgroundColor': 'transparent', 
                                    'border': '1px solid rgba(255, 255, 255, 0.2)', 
                                    'color': '#e5e7eb',
                                    'width': '100%',
                                    'textAlign': 'left',
                                    'padding': '0.75rem 1rem',
                                    'borderRadius': '0.75rem',
                                    'margin': '0.25rem 0'
                                }
                            ),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavLink([html.I(className="fas fa-leaf"), " Chl-a"], href="/esa/sentinel/olci", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                    ], vertical=True
                                ),
                                id="mobile-sentinel-collapse",
                                is_open=False,
                            ),
                            html.Hr(),
                            html.H2("UK Met Office (UKMO)", className="display-6", style={'fontSize': '18px'}),
                            dbc.NavLink([html.I(className="fas fa-cloud"), " SST"], href="/ukmo/ostia", style={'fontSize': '14px'}),
                            html.Hr(),
                            html.H2("NASA", className="display-6", style={'fontSize': '18px'}),
                            html.Button(
                                [html.I(className="fas fa-thermometer-half"), " GHRSST"], 
                                id="mobile-ghrsst-button", 
                                className="btn", 
                                n_clicks=0,
                                style={
                                    'fontSize': '16px',
                                    'backgroundColor': 'transparent', 
                                    'border': '1px solid rgba(255, 255, 255, 0.2)', 
                                    'color': '#e5e7eb',
                                    'width': '100%',
                                    'textAlign': 'left',
                                    'padding': '0.75rem 1rem',
                                    'borderRadius': '0.75rem',
                                    'margin': '0.25rem 0'
                                }
                            ),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavLink([html.I(className="fas fa-map"), " SST"], href="/nasa/ghrsst/mur", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                    ], vertical=True
                                ),
                                id="mobile-ghrsst-collapse",
                                is_open=False,
                            ),
                            html.Button(
                                [html.I(className="fas fa-satellite-dish"), " MODIS"], 
                                id="mobile-modis-button", 
                                className="btn", 
                                n_clicks=0,
                                style={
                                    'fontSize': '16px',
                                    'backgroundColor': 'transparent', 
                                    'border': '1px solid rgba(255, 255, 255, 0.2)', 
                                    'color': '#e5e7eb',
                                    'width': '100%',
                                    'textAlign': 'left',
                                    'padding': '0.75rem 1rem',
                                    'borderRadius': '0.75rem',
                                    'margin': '0.25rem 0'
                                }
                            ),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavLink([html.I(className="fas fa-leaf"), " POC"], href="/nasa/modis/poc", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-cube"), " PIC"], href="/nasa/modis/pic", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.NavLink([html.I(className="fas fa-lightbulb"), " PAR"], href="/nasa/modis/par", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                    ], vertical=True
                                ),
                                id="mobile-modis-collapse",
                                is_open=False,
                            ),
                            html.Hr(),
                            html.H2("Mercator Ocean International (MOI)", className="display-6", style={'fontSize': '18px'}),
                            html.Button(
                                [html.I(className="fas fa-cogs"), " MODEL"], 
                                id="mobile-model-button", 
                                className="btn", 
                                n_clicks=0,
                                style={
                                    'fontSize': '16px',
                                    'backgroundColor': 'transparent', 
                                    'border': '1px solid rgba(255, 255, 255, 0.2)', 
                                    'color': '#e5e7eb',
                                    'width': '100%',
                                    'textAlign': 'left',
                                    'padding': '0.75rem 1rem',
                                    'borderRadius': '0.75rem',
                                    'margin': '0.25rem 0'
                                }
                            ),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavLink([html.I(className="fas fa-fish"), html.B(" PISCES")], href="#", id="mobile-pisces-link", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.Collapse(
                                            dbc.Nav(
                                                [
                                                    dbc.NavLink([html.I(className="fas fa-dna"), " Bio"], href="/moi/model/pisces/bio", style={'fontSize': '14px', 'paddingLeft': '40px'}),
                                                    dbc.NavLink([html.I(className="fas fa-apple-alt"), " Nut"], href="/moi/model/pisces/nut", style={'fontSize': '14px', 'paddingLeft': '40px'}),
                                                    dbc.NavLink([html.I(className="fas fa-eye"), " Optics"], href="/moi/model/pisces/optics", style={'fontSize': '14px', 'paddingLeft': '40px'}),
                                                    dbc.NavLink([html.I(className="fas fa-leaf"), " Car"], href="/moi/model/pisces/car", style={'fontSize': '14px', 'paddingLeft': '40px'}),
                                                    dbc.NavLink([html.I(className="fas fa-cube"), " CO₂"], href="/moi/model/pisces/co2", style={'fontSize': '14px', 'paddingLeft': '40px'}),
                                                    dbc.NavLink([html.I(className="fas fa-seedling"), " PFTs"], href="/moi/model/pisces/pfts", style={'fontSize': '14px', 'paddingLeft': '40px'})
                                                ], vertical=True
                                            ),
                                            id="mobile-pisces-collapse",
                                            is_open=False,
                                        ),
                                        dbc.NavLink([html.I(className="fas fa-fish"), html.B(" SEAPODYM")], href="#", id="mobile-seapodym-link", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.Collapse(
                                            dbc.Nav(
                                                [
                                                    dbc.NavLink([html.I(className="fas fa-weight"), " Biomass"], href="/moi/model/seapodym/biomass", style={'fontSize': '14px', 'paddingLeft': '40px'})
                                                ], vertical=True
                                            ),
                                            id="mobile-seapodym-collapse",
                                            is_open=False,
                                        ),
                                        dbc.NavLink([html.I(className="fas fa-water"), html.B(" NEMO")], href="#", id="mobile-nemo-link", style={'fontSize': '14px', 'paddingLeft': '20px'}),
                                        dbc.Collapse(
                                            dbc.Nav(
                                                [
                                                    dbc.NavLink([html.I(className="fas fa-tint"), " Salinity"], href="/moi/model/nemo/salinity", style={'fontSize': '14px', 'paddingLeft': '40px'})
                                                ], vertical=True
                                            ),
                                            id="mobile-nemo-collapse",
                                            is_open=False,
                                        ),
                                    ], vertical=True
                                ),
                                id="mobile-model-collapse",
                                is_open=False,
                            ),
                        ]
                    ),
                    id="mobile-datasets-collapse",
                    is_open=False,
                ),
            ],
            id="mobile-sidebar-content",
            style={"display": "block"}
        ),
    ],
    id="mobile-sidebar",
    title="Navigation",
    placement="start",
    is_open=False,
    style={
        "width": "20rem",
        "background": "linear-gradient(180deg, #111827 0%, #374151 100%)"
    },
    className="d-md-none"  # Only show on mobile
)

# Content area
toggle_button = dbc.Button(
    html.I(className="fas fa-bars"),
    id="sidebar-toggle",
    style={"margin-left": "1rem", "margin-top": "1rem"},
    className="d-md-none"  # Only show on mobile
)

content = html.Div(id="page-content", style={"transition": "margin-left 0.3s"}, className="content")

# Main layout
layout = html.Div([dcc.Location(id="url"), toggle_button, sidebar, mobile_sidebar, content])
