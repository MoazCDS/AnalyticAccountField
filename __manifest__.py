{
    'name' : "account_analytic_field",
    'description': 'Account Analytic Field',
    'author' : "Moaz Elbahr",
    'category': '',
    'version': '18.0.0.1.0',
    'depends': ['base', 'purchase', 'accountant', 'account', 'sale_management'],
    'data': [
        "views/account_move_view.xml",
        "views/purchase_order_view.xml",
        "views/sale_order_view.xml",
    ],
}