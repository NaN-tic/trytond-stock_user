# This file is part of stock_user module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .user import *
from .product import *
from .shipment import *


def register():
    Pool.register(
        User,
        UserStockWarehouse,
        UserStockLocation,
        Product,
        ShipmentIn,
        ShipmentOut,
        ShipmentOutReturn,
        module='stock_user', type_='model')
