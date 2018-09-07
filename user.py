#This file is part stock_user module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields, ModelSQL
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval

__all__ = ['User', 'UserStockWarehouse', 'UserStockLocation']


class User(metaclass=PoolMeta):
    __name__ = "res.user"
    stock_warehouses = fields.Many2Many('res.user-warehouse', 'user',
        'warehouse', 'Warehouses',
        domain=[('type', '=', 'warehouse')],
        help='Default warehouses where user can be working on.')
    stock_warehouses_user = fields.Function(fields.Many2Many('stock.location',
        None, None, 'Warehouses User', states={'invisible': False}),
        'on_change_with_stock_warehouses_user')
    stock_warehouse = fields.Many2One('stock.location', "Warehouse",
        domain=[('id', 'in', Eval('stock_warehouses_user', []))],
        depends=['stock_warehouses_user'],
        help='Default warehouse where user is working on.')
    stock_locations = fields.Many2Many('res.user-stock_location', 'user',
        'location', 'Locations',
        help='Default locations where user can be working on.')

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()
        cls._preferences_fields.extend([
                'stock_warehouse',
                ])
        cls._context_fields.insert(0, 'stock_warehouses_user')
        cls._context_fields.insert(0, 'stock_warehouse')
        cls._context_fields.insert(0, 'stock_locations')

    def get_status_bar(self, name):
        status = super(User, self).get_status_bar(name)
        if self.stock_warehouse:
            status += ' - %s' % (self.stock_warehouse.rec_name)
        return status

    @fields.depends('stock_warehouses')
    def on_change_with_stock_warehouses_user(self, name=None):
        # if user have not warehouses, can view all warehouses
        Location = Pool().get('stock.location')
        if self.stock_warehouses:
            return [w.id for w in self.stock_warehouses]
        warehouses = Location.search([('type', '=', 'warehouse')])
        return [w.id for w in warehouses]


class UserStockWarehouse(ModelSQL):
    'User - Stock Warehouse'
    __name__ = 'res.user-warehouse'
    _table = 'res_user_warehouse'
    warehouse = fields.Many2One('stock.location', 'Warehouse',
        ondelete='CASCADE', select=True, required=True)
    user = fields.Many2One('res.user', 'User', ondelete='RESTRICT',
        select=True, required=True)


class UserStockLocation(ModelSQL):
    'User - Stock Location'
    __name__ = 'res.user-stock_location'
    _table = 'res_user_stock_location'
    location = fields.Many2One('stock.location', 'Location',
        ondelete='CASCADE', select=True, required=True)
    user = fields.Many2One('res.user', 'User', ondelete='RESTRICT',
        select=True, required=True)
