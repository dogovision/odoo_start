from odoo import fields, models
from odoo.exceptions import Warning


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'
    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN', help="Use a valid ISB-13 or ISBN-10")
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher', index=True)
    author_ids = fields.Many2many('res.partner', string='Authors')

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check
        
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning(f'Please provide an ISBN for {book.name}')
            elif not book._check_isbn():
                raise Warning(f'{book.isbn} is an invalid ISBN.')
        return True