from odoo import http
from oddo.addons.library_apps.controllers.main import Books

class BooksExtended(Books):
    @http.route()
    def list(self, **kwargs):
        response = super().list(**kwargs)
        if kwargs.get('available'):
            Book = http.request.env['library.book']
            books = Book.search([('is_available', '=', True)])
            response.qcontext['books'] = books
        return response
