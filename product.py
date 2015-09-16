#This file is part stock_user module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.transaction import Transaction

__metaclass__ = PoolMeta
__all__ = ['Product']


class Product:
    __name__ = 'product.product'

    @classmethod
    def get_quantity(cls, products, name):
        context = Transaction().context
        # not locations + stock_warehouse in context
        if 'locations' not in context and context.get('stock_warehouse'):
            location_ids = [context['stock_warehouse']]
            with Transaction().set_context(locations=location_ids):
                return cls._get_quantity(products, name, location_ids, products)
        # return super (with locations in context)
        return super(Product, cls).get_quantity(products, name)
