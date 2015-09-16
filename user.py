#This file is part stock_user module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields, ModelSQL
from trytond.pool import PoolMeta

__all__ = ['User', 'UserStockLocation']
__metaclass__ = PoolMeta


class User:
    __name__ = "res.user"
    stock_warehouse = fields.Many2One('stock.location', "Warehouse",
        domain=[('type', '=', 'warehouse')],
        help='Default warehouse where user is working on.')
    stock_locations = fields.Many2Many('res.user-stock_location', 'user',
        'location', 'Locations',
        domain=[('type', '=', 'storage')],
        help='Default location where user is working on.')

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()
        cls._preferences_fields.extend([
                'stock_warehouse',
                ])
        cls._context_fields.insert(0, 'stock_warehouse')
        cls._context_fields.insert(0, 'stock_locations')

    def get_status_bar(self, name):
        status = super(User, self).get_status_bar(name)
        if self.stock_warehouse:
            status += ' - %s' % (self.stock_warehouse.rec_name)
        return status


class UserStockLocation(ModelSQL):
    'User - Stock Location'
    __name__ = 'res.user-stock_location'
    _table = 'res_user_stock_location'
    location = fields.Many2One('stock.location', 'Location',
        ondelete='CASCADE', select=True, required=True)
    user = fields.Many2One('res.user', 'User', ondelete='RESTRICT',
        select=True, required=True)
