from odoo import fields, models

class Book(models.Model):
    _inherit = 'library.book'
    is_available = fields.Boolean('Is Available?', readonly=False)

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 10:
            ponderators = [x for x in range(1, 10)]
            total = sum(a * b for a, b in zip(digits[:9], ponderators))
            check = total % 11
            return digits[-1] == check
        else:
            return super()._check_isbn()
