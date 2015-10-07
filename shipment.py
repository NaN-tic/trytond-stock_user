# This file is part of the poolback module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import fields
from trytond.pyson import Bool, Eval, If
from trytond.transaction import Transaction

__all__ = ['ShipmentIn', 'ShipmentOut', 'ShipmentOutReturn']
__metaclass__ = PoolMeta


class ShipmentMixin(object):
    warehouse_domain = fields.Function(fields.Many2One('stock.location',
            'Wharehouse Domain',
            states={
                'invisible': False,
                }),
        'on_change_with_warehouse_domain')

    @classmethod
    def default_warehouse(cls):
        User = Pool().get('res.user')
        user = User(Transaction().user)
        if user.stock_warehouse:
            return user.stock_warehouse.id

    def on_change_with_warehouse_domain(self, name):
        User = Pool().get('res.user')
        user = User(Transaction().user)
        return user.stock_warehouse.id if user.stock_warehouse else None


class ShipmentIn(ShipmentMixin):
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.in'

    @classmethod
    def __setup__(cls):
        super(ShipmentIn, cls).__setup__()
        warehouse_domain = If(Bool(Eval('warehouse_domain', 0)),
            ('id', '=', Eval('warehouse_domain')),
            ('id', '>', -1))
        cls.warehouse.domain.append(warehouse_domain)
        cls.warehouse.depends.append('warehouse_domain')

    @classmethod
    def default_warehouse(cls):
        warehouse = ShipmentMixin.default_warehouse()
        if warehouse:
            return warehouse
        return super(ShipmentIn, cls).default_warehouse()


class ShipmentOut(ShipmentMixin):
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out'

    @classmethod
    def __setup__(cls):
        super(ShipmentOut, cls).__setup__()
        warehouse_domain = If(Bool(Eval('warehouse_domain', 0)),
            ('id', '=', Eval('warehouse_domain')),
            ('id', '>', -1))
        cls.warehouse.domain.append(warehouse_domain)
        cls.warehouse.depends.append('warehouse_domain')

    @classmethod
    def default_warehouse(cls):
        warehouse = ShipmentMixin.default_warehouse()
        if warehouse:
            return warehouse
        return super(ShipmentOut, cls).default_warehouse()


class ShipmentOutReturn(ShipmentMixin):
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out.return'

    @classmethod
    def __setup__(cls):
        super(ShipmentOutReturn, cls).__setup__()
        warehouse_domain = If(Bool(Eval('warehouse_domain', 0)),
            ('id', '=', Eval('warehouse_domain')),
            ('id', '>', -1))
        cls.warehouse.domain.append(warehouse_domain)
        cls.warehouse.depends.append('warehouse_domain')

    @classmethod
    def default_warehouse(cls):
        warehouse = ShipmentMixin.default_warehouse()
        if warehouse:
            return warehouse
        return super(ShipmentOutReturn, cls).default_warehouse()
