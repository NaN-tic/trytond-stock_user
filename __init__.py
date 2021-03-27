# This file is part of stock_user module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import user
from . import product
from . import shipment


def register():
    Pool.register(
        user.User,
        user.UserStockWarehouse,
        user.UserStockLocation,
        product.Product,
        shipment.ShipmentIn,
        shipment.ShipmentOut,
        shipment.ShipmentOutReturn,
        module='stock_user', type_='model')
