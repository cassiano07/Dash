from dash import html
import dash_bootstrap_components as bc


def navbar():
    logo = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

    # select
    coins = ['AAVE', 'ACMFT', 'ACORDO01', 'ADA', 'ALCX', 'ALGO', 'ALICE', 'ALLFT', 'AMFT', 'AMP', 'ANKR', 'ANT',
             'ARGFT', 'ASRFT', 'ATMFT', 'ATOM', 'AUDIO', 'AVAX', 'AXS', 'BAL', 'BAND', 'BARFT', 'BAT', 'BCH', 'BLZ',
             'BNT', 'BTC', 'CAIFT', 'CHZ', 'CITYFT', 'COMP', 'CRV', 'CSCONS01', 'CTSI', 'CVX', 'DAI', 'DOGE', 'DOT',
             'DYDX', 'ENJ', 'ENS', 'ETH', 'FET', 'FIL', 'FLOKI', 'GALA', 'GALFT', 'GALOFT', 'GNO', 'GODS', 'GRT', 'ICP',
             'ILV', 'IMOB01', 'IMOB02', 'IMX', 'INTERFT', 'JUVFT', 'KEEP', 'KNC', 'KP3R', 'LDO', 'LINK', 'LOOKS', 'LPT',
             'LQTY', 'LRC', 'LTC', 'MANA', 'MATIC', 'MBCCSH01', 'MBCCSH02', 'MBCONS01', 'MBCONS02', 'MBFP01', 'MBFP02',
             'MBFP03', 'MBFP04', 'MBFP05', 'MBPRK01', 'MBPRK02', 'MBPRK03', 'MBPRK04', 'MBPRK05', 'MBPRK06', 'MBPRK07',
             'MBSANTOS01', 'MBVASCO01', 'MC', 'MCO2', 'MENGOFT', 'MIR', 'MKR', 'NAVIFT', 'NFT00', 'NFT10', 'NFT11',
             'NFT12', 'NFT13', 'NFT14', 'NFT15', 'NFT16', 'NFT17', 'NFT18', 'NFT2', 'NFT3', 'NFT4', 'NFT5', 'NFT6',
             'NFT7', 'NFT8', 'NFT9', 'NFTOKN01', 'OCEAN', 'OGFT', 'OGN', 'OMG', 'OPUL', 'OXT', 'PAXG', 'PERP', 'PFLFT',
             'PLA', 'POLS', 'PORFT', 'PSGFT', 'QNT', 'RACA', 'RAD', 'RARI', 'REN', 'REQ', 'RLY', 'RNDR', 'SACI', 'SAND',
             'SAUBERFT', 'SCCPFT', 'SHIB', 'SKL', 'SLP', 'SNX', 'SOL', 'SPELL', 'SPFCFT', 'STVFT', 'SUPER', 'SUSHI',
             'SYN', 'THFT', 'TRU', 'UFCFT', 'UMA', 'UNI', 'USDC', 'USDP', 'VERDAO', 'VSPRK01', 'WBTC', 'WBX', 'WLUNA',
             'XLM', 'XRP', 'XTZ', 'YBOFT', 'YFI', 'YGG', 'ZRX']

    # Criar select de coins
    select = bc.Select(
        id="select",
        options=[{"label": coin, "value": coin} for coin in coins],
        value="BTC"
    )

    # montar o search para adicionar na navbar
    search_bar = bc.Row(
        [
            bc.Col(select),
            bc.Col(
                bc.Button(
                    "Search", color="primary", className="ms-2", n_clicks=0, id='submit-button', type='submit',
                ),
                width="auto",
            ),
        ],
        className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )

    nav = bc.Navbar(
        bc.Container(
            [
                html.A(
                    bc.Row(
                        [
                            bc.Col(html.Img(src=logo, height="30px")),
                            bc.Col(bc.NavbarBrand("Last 1000 trades", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    style={"textDecoration": "none"},
                ),
                bc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                bc.Collapse(
                    search_bar,
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
        style={"width": "100%"}
    )

    return nav


