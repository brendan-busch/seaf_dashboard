from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.colors

# Function to generate the data for the sunburst chart
def generate_sunburst_data():
    data = [
        ["ESA", "Globcolor", "Reflectance", "RRS412, RRS443, RRS490, RRS555, RRS670"],
        ["ESA", "Globcolor", "Optics", "BBP, CDM"],
        ["ESA", "Globcolor", "Transp", "KD490, ZSD, SPM"],
        ["ESA", "Globcolor", "Plankton", "CHL, DIATO, DINO, GREEN, HAPTO, MICRO, NANO, PICO, PROCHLO, PROKAR"],
        ["ESA", "Globcolor", "PP", "PP"],
        ["ESA", "Sentinel", "OLCI", "Chl-a"],
        ["UKMO", "UKMO", "OSTIA", "Temp"],
        ["NASA", "MODIS", "MODIS", "POC, PIC, PAR"],
        ["NASA", "GHRSST", "MUR", "SST"],
        ["MOI", "PISCES", "BIO", "NPPV, O₂"],
        ["MOI", "PISCES", "NUT", "Fe, NO₃, PO₄, Si"],
        ["MOI", "PISCES", "OPTICS", "KD"],
        ["MOI", "PISCES", "Car", "DIC, PH, Talk"],
        ["MOI", "PISCES", "CO₂", "spCO₂"],
        ["MOI", "PISCES", "PFTs", "CHL, Phyto"],
        ["MOI", "SEAPODYM", "Biomass", "PP, ZOO"],
        ["MOI", "NEMO", "SAL", "Salinity"]
    ]

    labels = ["Datasets"]  # Starting point for the hierarchy
    parents = [""]    # The root has no parent

    for agency, program, category, variables in data:
        if agency not in labels:
            labels.append(agency)
            parents.append("Datasets")

        if program not in labels:
            labels.append(program)
            parents.append(agency)

        if category not in labels:
            labels.append(category)
            parents.append(program)

        for variable in variables.split(", "):
            if variable not in labels:
                labels.append(variable)
                parents.append(category)

    return labels, parents

# Function to create the sunburst chart
def create_sunburst_chart():
    labels, parents = generate_sunburst_data()
    fig = go.Figure(go.Sunburst(
        labels=labels,
        parents=parents,
        branchvalues="total",
        marker=dict(colors=plotly.colors.qualitative.Pastel)  # Applying a color scheme
    ))
    #fig.update_traces(textinfo='label+percent entry')
    fig.update_layout(
        margin=dict(t=50, l=0, r=0, b=0),
        title=dict(
            text="Available Datasets",
            x=0.5,  # Center the title
            xanchor='center',
            yanchor='top',
            font=dict(
                size=24,  # Increase the font size
                family="Times New Roman",  # Set the font to Times New Roman
                weight="bold",
                color="black"  # Set the font color to black
            )
        )
    )
    return fig

# Define the layout for the Dash application
def home_layout():
    return html.Div([
        # Header with background image
        html.Div([
            html.H1("Data Visualization Dashboard", className="display-3 text-white"),
            html.H5("Based on Satellite and MODEL Output", className="display-7 text-white"),
            html.P(
                "Explore the distribution of environmental datasets from agencies like NASA, ESA, UKMO, and MOI for the region of Cockburn Sound (CS).",
                className="lead text-white"
            ),
        ], className="header-section"),
        # Add a button to open the guide modal
        html.Div([
            dbc.Button("🚀 How to Explore the Dashboard", 
                       id="open-guide-modal", 
                       className="bounce-animated delayed-start mb-4 guide-button",
                       color="primary"
            ),
        ], style={"text-align": "center"}),

        # Guide Modal
        dbc.Modal([
            dbc.ModalHeader("🌟 Dashboard Guide"),
            dbc.ModalBody([
                html.H5("Welcome to the Dashboard!"),
                html.P("This dashboard presents environmental datasets collected from various agencies. Here's how you can make the most out of it:"),
                        html.Ul([
                            html.Li([
                                "Use the sidebar to navigate different datasets by clicking the ", 
                                html.Span([
                                    html.I(className="fas fa-database", style={"margin-right": "5px"}),
                                    html.B("Datasets")
                                ], style={"color": "green"}), 
                                " button."
                            ]),
                            html.Li([
                                "In each dataset layout, click the ", 
                                html.B("About"), 
                                " section to learn more about the dataset properties, source, and data processing."
                            ]),
                            html.Li([
                                "Click on the map layer (left side) under each layout and explore dataset positions as well as the WMS layer."
                            ]),
                            html.Li([
                                "Use the dropdowns and filters to customize your view of the data."
                            ]),
                        ], className="custom-list"),
                html.P("Feel free to reach out for further assistance using the contact links below."),
                html.P([
                    html.I(className="fas fa-envelope", style={"color": "blue", "margin-right": "5px"}),
                    html.A("Md Rony Golder", href="mailto:mdrony.golder@uwa.edu.au", style={"color": "blue"})
                ])
            ]),
            dbc.ModalFooter(
                dbc.Button("Close", id="close-guide-modal", className="ml-auto", color="secondary")
            ),
        ], id="guide-modal", is_open=False),

        # Cards for key information
        dbc.Container([
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("Agencies", className="card-title card-title-text"),
                        html.P("4", className="card-text card-text-circle")
                    ])
                ], className="card agencies-card"), width=12, md=4),
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("Total Datasets", className="card-title card-title-text"),
                        html.P("17", className="card-text card-text-circle")
                    ])
                ], className="card total-datasets-card"), width=12, md=4),
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("Variables", className="card-title card-title-text"),
                        html.P("43", className="card-text card-text-circle")
                    ])
                ], className="card variables-card"), width=12, md=4),
            ], className="mb-4"),
        ]),

        # Sunburst chart and agencies description
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H4("Agencies", className="agencies-title"),  # Heading
                        html.Ul([  # Unordered list
                            html.Li([html.Span("ESA: ", className="list-bold"), "European Space Agency"]),
                            html.Li([html.Span("NASA: ", className="list-bold"), "National Aeronautics and Space Administration"]),
                            html.Li([html.Span("UKMO: ", className="list-bold"), "United Kingdom Meteorological Office"]),
                            html.Li([html.Span("MOI: ", className="list-bold"), "Mercator Ocean International"])
                        ], className="agencies-list"),  # Add space between lists
                        html.H4("Programs",  className="programs-title"),  # Heading
                        html.Ul([  # Unordered list
                            html.Li([html.Span("GlobColour: ", className="list-bold"), "Global Ocean Colour"]),
                            html.Li([html.Span("GHRSST: ", className="list-bold"), "Group for High Resolution Sea Surface Temperature"]),
                            html.Li([html.Span("NEMO: ", className="list-bold"), "Nucleus for European Modelling of the Ocean"]),
                            html.Li([html.Span("PISCES: ", className="list-bold"), "Pelagic Interactions Scheme for Carbon and Ecosystem Studies"]),
                            html.Li([html.Span("SEAPODYM: ", className="list-bold"), "Spatial Ecosystem and Population Dynamics Model"]),
                            html.Li([html.Span("MODIS: ", className="list-bold"), "Moderate Resolution Imaging Spectroradiometer"]),
                            html.Li([html.Span("OLCI: ", className="list-bold"), "Ocean and Land Colour Instrument"]),
                            html.Li([html.Span("OSTIA: ", className="list-bold"), "Operational Sea Surface Temperature and Sea Ice Analysis"]),
                        ], className="programs-list")  # Add space between lists
                    ], className="agencies-description")  # Right column with the full forms
                ], width=12, md=6),
                dbc.Col([
                    dcc.Graph(figure=create_sunburst_chart()),  # Left column with the figure
                ], width=12, md=6)
            ], className="sunburst-section"),
        ]),

        # Interactive map with title
        dbc.Container([
            dbc.Row([
                dbc.Col(html.H4("Dataset Position Map", className="text-center mb-4"), width=12)
            ]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Iframe(
                        src="https://curtin.maps.arcgis.com/apps/instant/basic/index.html?appid=dd40758d043c4871bc6aedfc6bd178c8",
                        style={"border": "0", "width": "100%", "height": "600px"},
                    ),
                    html.P("iFrames are not supported on this page.", style={"display": "none"})
                ]), width=12)
            ])
        ], style={"margin-bottom": "20px"}),

        # Footer with contact information
        html.Div([
            # Main footer content with responsive layout
            html.Div([
                # Left section: WAMSI logo and social media icons
                html.Div([
                    html.A(
                        html.Img(
                            src="assets/wamsi-logo.png",
                            className="footer-logo"
                        ),
                        href="https://www.wamsi.org.au", 
                        target="_blank"
                    ),
                    html.Div([
                        html.A(
                            html.I(className="fab fa-facebook-f"),
                            href="https://www.facebook.com/WesternAustralianMarineScience", 
                            target="_blank",
                            style={"color": "#4267B2"}
                        ),
                        html.A(
                            html.I(className="fab fa-youtube"),
                            href="https://www.youtube.com/user/WAMSIHQ", 
                            target="_blank",
                            style={"color": "#FF0000"}
                        ),
                        html.A(
                            html.I(className="fab fa-linkedin"),
                            href="https://www.linkedin.com/company/wamsi/", 
                            target="_blank",
                            style={"color": "#0A66C2"}
                        ),
                        html.A(
                            html.I(className="fab fa-instagram"),
                            href="https://www.instagram.com/westernaustralianmarinescience", 
                            target="_blank",
                            style={"color": "#E1306C"}
                        ),
                    ], className="footer-social-icons")
                ], className="footer-left"),
                
                # Center: Decorative separator (only visible on desktop)
                html.Div(className="footer-center"),
                
                # Right section: Links and copyright
                html.Div([
                    html.Div([
                        html.A([
                            html.I(className="fab fa-github"),
                            "View Source Code"
                        ], href="https://github.com/ronygolderku/seaf_dashboard", target="_blank"),
                        html.A([
                            html.I(className="fas fa-envelope"),
                            "Md Rony Golder"
                        ], href="mailto:mdrony.golder@uwa.edu.au"),
                    ], className="footer-links"),
                    html.P("© 2025 Md Rony Golder. All rights reserved.", className="footer-copyright")
                ], className="footer-right")
            ], className="footer-desktop-layout"),
            
            # Acknowledgment section
            html.P(
                "WAMSI acknowledges the traditional custodians of Country throughout Western Australia and their "
                "continuing connection to land, culture and community. We pay our respects to elders past and present.",
                className="footer-acknowledgment"
            )
        ], className="footer")
    ])