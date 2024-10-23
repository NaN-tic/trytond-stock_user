#This file is part stock_user module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
import datetime
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction


class Product(metaclass=PoolMeta):
    __name__ = 'product.product'

    @classmethod
    def get_quantity(cls, products, name):
        pool = Pool()
        Location = pool.get('stock.location')
        Date = pool.get('ir.date')

        stock_date = Date.today() if name == 'product' else datetime.date.max
        context = Transaction().context

        # not locations + stock_warehouse in context
        if not context.get('locations') and context.get('stock_warehouse'):
            warehouse = Location(context['stock_warehouse'])
            location_ids = [warehouse.storage_location.id, warehouse.input_location.id]
            product_ids = list(map(int, products))
            with Transaction().set_context(locations=location_ids,
                    stock_date_end=stock_date, with_childs=True):
                return cls._get_quantity(products, name, location_ids, grouping_filter=(product_ids,))
        # return super (with locations in context)
        return super(Product, cls).get_quantity(products, name)

    @classmethod
    def search_quantity(cls, name, domain=None):
        pool = Pool()
        Location = pool.get('stock.location')
        Date = pool.get('ir.date')

        stock_date = Date.today() if name == 'product' else datetime.date.max
        context = Transaction().context

        # not locations + stock_warehouse in context
        if not context.get('locations') and context.get('stock_warehouse'):
            warehouse = Location(context['stock_warehouse'])
            location_ids = [warehouse.storage_location.id, warehouse.input_location.id]
            with Transaction().set_context(locations=location_ids,
                    stock_date_end=stock_date, with_childs=True):
                return cls._search_quantity(name, location_ids, domain)
        # return super (with locations in context)
        return super(Product, cls).search_quantity(name, domain)
