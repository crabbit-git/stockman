from models.manufacturer import Manufacturer
from models.product import Product

from repositories import manufacturer_repository, product_repository

product_repository.delete_all()
manufacturer_repository.delete_all()

topre = Manufacturer("Topre", "JP")
manufacturer_repository.save(topre)

pfu = Manufacturer("PFU", "JP")
manufacturer_repository.save(pfu)

leopold = Manufacturer("Leopold", "KR")
manufacturer_repository.save(leopold)

rf108i = Product(
    'REALFORCE R2SA-US4-IV PFU Limited Edition (ivory)',
    'High-end 108-key keyboard exclusively manufactured by Topre to PFU\'s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer. Keycaps have high quality dye-sublimated legends.',
    4,
    180.00,
    216.66,
    topre
)
product_repository.save(rf108i)

rf108b = Product(
    'REALFORCE R2SA-US4-BK PFU Limited Edition (black)',
    'High-end 108-key keyboard exclusively manufactured by Topre to PFU\'s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer. Keycaps have high quality dye-sublimated legends.',
    4,
    rf108i.cost,
    rf108i.price,
    topre
)
product_repository.save(rf108b)

rf87i = Product(
    'REALFORCE R2TLSA-US4-IV PFU Limited Edition (ivory)',
    'High-end 87-key keyboard exclusively manufactured by Topre to PFU\'s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer. Keycaps have high quality dye-sublimated legends.',
    8,
    rf108i.cost,
    rf108i.price,
    topre
)
product_repository.save(rf87i)

rf87b = Product(
    'REALFORCE R2TLSA-US4-BK PFU Limited Edition (black)',
    'High-end 87-key keyboard exclusively manufactured by Topre to PFU\'s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer. Keycaps have high quality dye-sublimated legends.',
    8,
    rf108i.cost,
    rf108i.price,
    topre
)
product_repository.save(rf87b)

hhkbcw = Product(
    'HHKB Professional Classic PD-KB401W (white, printed keycaps)',
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    130.00,
    164.99,
    pfu
)
product_repository.save(hhkbcw)

hhkbcwn = Product(
    'HHKB Professional Classic PD-KB401WN (white, blank keycaps)',
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    hhkbcw.cost,
    hhkbcw.price,
    pfu
)
product_repository.save(hhkbcwn)

hhkbcc = Product(
    'HHKB Professional Classic PD-KB401B (charcoal, printed keycaps)',
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    hhkbcw.cost,
    hhkbcw.price,
    pfu
)
product_repository.save(hhkbcc)

hhkbccn = Product(
    'HHKB Professional Classic PD-KB401BN (charcoal, blank keycaps)',
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    hhkbcw.cost,
    hhkbcw.price,
    pfu
)
product_repository.save(hhkbccn)

hhkbhw = Product(
    'HHKB Professional Hybrid PD-KB800W (white, printed keycaps)',
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    160.00,
    194.99,
    pfu
)
product_repository.save(hhkbhw)

hhkbhwn = Product(
    'HHKB Professional Hybrid PD-KB800WN (white, blank keycaps)',
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    hhkbhw.cost,
    hhkbhw.price,
    pfu
)
product_repository.save(hhkbhwn)

hhkbhc = Product(
    'HHKB Professional Hybrid PD-KB800B (charcoal, printed keycaps)',
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    hhkbhw.cost,
    hhkbhw.price,
    pfu
)
product_repository.save(hhkbhc)

hhkbhcn = Product(
    'HHKB Professional Hybrid PD-KB800BN (charcoal, blank keycaps)',
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    hhkbhw.cost,
    hhkbhw.price,
    pfu
)
product_repository.save(hhkbhcn)

hhkbsw = Product(
    'HHKB Professional Hybrid Type-S PD-KB800WS (white, printed keycaps)',
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced, 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    185.00,
    224.99,
    pfu
)
product_repository.save(hhkbsw)

hhkbswn = Product(
    'HHKB Professional Hybrid Type-S PD-KB800WNS (white, blank keycaps)',
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced, 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features blank keycaps.',
    6,
    hhkbsw.cost,
    hhkbsw.price,
    pfu
)
product_repository.save(hhkbswn)

hhkbsc = Product(
    'HHKB Professional Hybrid Type-S PD-KB800BS (charcoal, printed keycaps)',
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced, 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    hhkbsw.cost,
    hhkbsw.price,
    pfu
)
product_repository.save(hhkbsc)

hhkbscn = Product(
    'HHKB Professional Hybrid Type-S PD-KB800BNS (charcoal, blank keycaps)',
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced, 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features blank keycaps.',
    6,
    hhkbsw.cost,
    hhkbsw.price,
    pfu
)
product_repository.save(hhkbscn)

hhkbsnow = Product(
    'HHKB Professional Hybrid Type-S Snow Limited Edition PD-KB800YS (pure white, printed keycaps)',
    'The exclusive Snow model released for the HHKB\'s 25th anniversary is a pure white version of the HYBRID Type-S and includes a limited edition HHKB25 \'FN\' key, making it a unique piece of HHKB history. Only 250 units made available to the EMEA market area.',
    1,
    200.00,
    239.99,
    pfu
)
product_repository.save(hhkbsnow)

leow = Product(
    'Leopold FC660C (white)',
    '66-key keyboard manufactured by Leopold. Features 45 g capacitive Topre key switches and dye-sublimated keycap legends.',
    0,
    180.00,
    216.66,
    leopold
)
product_repository.save(leow)

leob = Product(
    'Leopold FC660C (black)',
    '66-key keyboard manufactured by Leopold. Features 45 g capacitive Topre key switches and dye-sublimated keycap legends.',
    0,
    leow.cost,
    leow.price,
    leopold
)
product_repository.save(leob)

breakpoint()
