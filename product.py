#This file is part stock_user module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['Product']


class Product:
    __metaclass__ = PoolMeta
    __name__ = 'product.product'

    @classmethod
    def get_quantity(cls, products, name):
        Location = Pool().get('stock.location')

        context = Transaction().context
        # not locations + stock_warehouse in context
        if not context.get('locations') and context.get('stock_warehouse'):
            warehouse = Location(context['stock_warehouse'])
            location_ids = [warehouse.storage_location.id, warehouse.input_location.id]
            product_ids = map(int, products)
            with Transaction().set_context(locations=location_ids):
                return cls._get_quantity(products, name, location_ids, grouping_filter=(product_ids,))
        # return super (with locations in context)
        return super(Product, cls).get_quantity(products, name)

    @classmethod
    def search_quantity(cls, name, domain=None):
        Location = Pool().get('stock.location')
        context = Transaction().context
        # not locations in context
        if not context.get('locations') and context.get('stock_warehouse'):
            warehouse = Location(context['stock_warehouse'])
            location_ids = [warehouse.storage_location.id, warehouse.input_location.id]
            with Transaction().set_context(locations=location_ids):
                return cls._search_quantity(name, location_ids, domain)
        # return super (with locations in context)
        return super(Product, cls).search_quantity(name, domain)
