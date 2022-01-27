from dash import html
import dash_bootstrap_components as bc


def navbar():
    logo = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

    nav = bc.Navbar(
        bc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    bc.Row(
                        [
                            bc.Col(html.Img(src=logo, height="30px")),
                            bc.Col(bc.NavbarBrand("Daniel Cassiano", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="https://localhost",
                    style={"textDecoration": "none"},
                ),
                bc.Collapse(
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
    )

    return nav
