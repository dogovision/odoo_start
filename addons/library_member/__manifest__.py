{
    'name': 'Library Members',
    'description': 'Manage people who will be able to borrow books.',
    'author': 'Tavo tevas',
    'depends': ['library_app'],
    'application': False,
    'data': [
        'security/library_security.xml',
        'views/book_view.xml'
    ]
}