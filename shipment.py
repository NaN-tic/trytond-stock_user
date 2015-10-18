# This file is part of the poolback module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval
from trytond.transaction import Transaction

__all__ = ['ShipmentIn', 'ShipmentOut', 'ShipmentOutReturn']
__metaclass__ = PoolMeta


class ShipmentIn:
    __name__ = 'stock.shipment.in'

    @classmethod
    def __setup__(cls):
        super(ShipmentIn, cls).__setup__()
        warehouse_domain =  ('id', 'in', Eval('context', {}).get(
                'stock_warehouses_user', []))
        cls.warehouse.domain.append(warehouse_domain)

    @classmethod
    def default_warehouse(cls):
        User = Pool().get('res.user')
        user = User(Transaction().user)
        if user.stock_warehouse:
            return user.stock_warehouse.id


class ShipmentOut:
    __name__ = 'stock.shipment.out'

    @classmethod
    def __setup__(cls):
        super(ShipmentOut, cls).__setup__()
        warehouse_domain =  ('id', 'in', Eval('context', {}).get(
                'stock_warehouses_user', []))
        cls.warehouse.domain.append(warehouse_domain)

    @classmethod
    def default_warehouse(cls):
        User = Pool().get('res.user')
        user = User(Transaction().user)
        if user.stock_warehouse:
            return user.stock_warehouse.id


class ShipmentOutReturn:
    __name__ = 'stock.shipment.out.return'

    @classmethod
    def __setup__(cls):
        super(ShipmentOutReturn, cls).__setup__()
        warehouse_domain =  ('id', 'in', Eval('context', {}).get(
                'stock_warehouses_user', []))
        cls.warehouse.domain.append(warehouse_domain)

    @classmethod
    def default_warehouse(cls):
        User = Pool().get('res.user')
        user = User(Transaction().user)
        if user.stock_warehouse:
            return user.stock_warehouse.id
