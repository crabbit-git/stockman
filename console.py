from models.category import Category
from models.manufacturer import Manufacturer
from models.product import Product

from repositories import category_repository, manufacturer_repository, product_repository

product_repository.delete_all()
manufacturer_repository.delete_all()
category_repository.delete_all()

keyboards = Category('Keyboards')
category_repository.save(keyboards)

parts = Category('Parts')
category_repository.save(parts)

topre = Manufacturer("Topre", "JP")
manufacturer_repository.save(topre)

pfu = Manufacturer("PFU", "JP")
manufacturer_repository.save(pfu)

leopold = Manufacturer("Leopold", "KR")
manufacturer_repository.save(leopold)

deskeys = Manufacturer("Deskeys", "CN")
manufacturer_repository.save(deskeys)

rf108i = Product(
    "REALFORCE R2SA-US4-IV PFU Limited Edition (ivory)",
    keyboards,
    "High-end 108-key keyboard exclusively manufactured by Topre to PFU's specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer. Keycaps have high quality dye-sublimated legends.",
    4,
    180.00,
    216.66,
    topre
)
product_repository.save(rf108i)

rf108b = Product(
    "REALFORCE R2SA-US4-BK PFU Limited Edition (black)",
    keyboards,
    "High-end 108-key keyboard exclusively manufactured by Topre to PFU's specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer. Keycaps have high quality dye-sublimated legends.",
    4,
    rf108i.cost,
    rf108i.price,
    topre
)
product_repository.save(rf108b)

rf87i = Product(
    "REALFORCE R2TLSA-US4-IV PFU Limited Edition (ivory)",
    keyboards,
    "High-end 87-key keyboard exclusively manufactured by Topre to PFU's specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer. Keycaps have high quality dye-sublimated legends.",
    8,
    rf108i.cost,
    rf108i.price,
    topre
)
product_repository.save(rf87i)

rf87b = Product(
    "REALFORCE R2TLSA-US4-BK PFU Limited Edition (black)",
    keyboards,
    "High-end 87-key keyboard exclusively manufactured by Topre to PFU's specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer. Keycaps have high quality dye-sublimated legends.",
    8,
    rf108i.cost,
    rf108i.price,
    topre
)
product_repository.save(rf87b)

hhkbcw = Product(
    "HHKB Professional Classic PD-KB401W (white, printed keycaps)",
    keyboards,
    "The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.",
    6,
    130.00,
    164.99,
    pfu
)
product_repository.save(hhkbcw)

hhkbcwn = Product(
    "HHKB Professional Classic PD-KB401WN (white, blank keycaps)",
    keyboards,
    "The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.",
    6,
    hhkbcw.cost,
    hhkbcw.price,
    pfu
)
product_repository.save(hhkbcwn)

hhkbcc = Product(
    "HHKB Professional Classic PD-KB401B (charcoal, printed keycaps)",
    keyboards,
    "The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.",
    6,
    hhkbcw.cost,
    hhkbcw.price,
    pfu
)
product_repository.save(hhkbcc)

hhkbccn = Product(
    "HHKB Professional Classic PD-KB401BN (charcoal, blank keycaps)",
    keyboards,
    "The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.",
    6,
    hhkbcw.cost,
    hhkbcw.price,
    pfu
)
product_repository.save(hhkbccn)

hhkbhw = Product(
    "HHKB Professional Hybrid PD-KB800W (white, printed keycaps)",
    keyboards,
    "Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.",
    6,
    160.00,
    194.99,
    pfu
)
product_repository.save(hhkbhw)

hhkbhwn = Product(
    "HHKB Professional Hybrid PD-KB800WN (white, blank keycaps)",
    keyboards,
    "Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.",
    6,
    hhkbhw.cost,
    hhkbhw.price,
    pfu
)
product_repository.save(hhkbhwn)

hhkbhc = Product(
    "HHKB Professional Hybrid PD-KB800B (charcoal, printed keycaps)",
    keyboards,
    "Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.",
    6,
    hhkbhw.cost,
    hhkbhw.price,
    pfu
)
product_repository.save(hhkbhc)

hhkbhcn = Product(
    "HHKB Professional Hybrid PD-KB800BN (charcoal, blank keycaps)",
    keyboards,
    "Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.",
    6,
    hhkbhw.cost,
    hhkbhw.price,
    pfu
)
product_repository.save(hhkbhcn)

hhkbsw = Product(
    "HHKB Professional Hybrid Type-S PD-KB800WS (white, printed keycaps)",
    keyboards,
    "Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced, 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features dye-sublimated keycap legends.",
    6,
    185.00,
    224.99,
    pfu
)
product_repository.save(hhkbsw)

hhkbswn = Product(
    "HHKB Professional Hybrid Type-S PD-KB800WNS (white, blank keycaps)",
    keyboards,
    "Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced, 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features blank keycaps.",
    6,
    hhkbsw.cost,
    hhkbsw.price,
    pfu
)
product_repository.save(hhkbswn)

hhkbsc = Product(
    "HHKB Professional Hybrid Type-S PD-KB800BS (charcoal, printed keycaps)",
    keyboards,
    "Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced, 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features dye-sublimated keycap legends.",
    6,
    hhkbsw.cost,
    hhkbsw.price,
    pfu
)
product_repository.save(hhkbsc)

hhkbscn = Product(
    "HHKB Professional Hybrid Type-S PD-KB800BNS (charcoal, blank keycaps)",
    keyboards,
    "Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced, 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features blank keycaps.",
    6,
    hhkbsw.cost,
    hhkbsw.price,
    pfu
)
product_repository.save(hhkbscn)

hhkbsnow = Product(
    "HHKB Professional Hybrid Type-S Snow Limited Edition PD-KB800YS (pure white, printed keycaps)",
    keyboards,
    "The exclusive Snow model released for the HHKB\'s 25th anniversary is a pure white version of the HYBRID Type-S and includes a limited edition HHKB25 \"FN\" key, making it a unique piece of HHKB history. Only 250 units made available to the EMEA market area.",
    0,
    200.00,
    239.99,
    pfu
)
product_repository.save(hhkbsnow)

leow = Product(
    "Leopold FC660C (white)",
    keyboards,
    "66-key keyboard manufactured by Leopold. Features 45 g capacitive Topre key switches and dye-sublimated keycap legends.",
    0,
    180.00,
    216.66,
    leopold
)
product_repository.save(leow)

leob = Product(
    "Leopold FC660C (black)",
    keyboards,
    "66-key keyboard manufactured by Leopold. Features 45 g capacitive Topre key switches and dye-sublimated keycap legends.",
    0,
    leow.cost,
    leow.price,
    leopold
)
product_repository.save(leob)

dess = Product(
    "DES-Sliders",
    parts,
    "Custom, Cherry MX keycap compatible replacement sliders for Topre keyboards. Made of Polyoxymethylene (POM) and manufactured within extremely strict tolerances, these are designed to fit more snugly than stock Topre sliders while also exhibiting less friction when actuated. They are also designed to allow enough space on the slider such that 0.5 mm silencing rings will result in a total key travel distance of 3.8 mm, which is the same as a HHKB Type-S (but 0.2 mm less than silenced REALFORCE/Leopold or unsilenced Topre). Each kit contains 102 1u sliders, 7 2u stabiliser-sliders, and 1 set of space bar stabiliser sliders and housings. Use the original stabiliser wires from a Topre keyboard on stabilised keys. IMPORTANT: If using these in any \"silenced\" Topre keyboard other than a Type-S HHKB, you will need to source replacement housings for keys larger than 1u. This is because silenced Topre keyboards use different housings and sliders for the 2u stabilisers in order to accommodate the 1 mm silencing rings they come with to avoid a reduction in key travel. HHKB Type-S keyboards use 0.5 mm silencing rings on the 2u keys, exactly the same as the ones on the 1u keys, and only the sliders (not the housings as well) are adjusted to partially compensate. Please bear this in mind if you plan to use DES-Sliders in any other silenced Topre keyboard, including REALFORCE and Leopold boards. RETURNS WILL NOT BE ACCEPTED ON THE BASIS OF INCOMPATIBILITY WITH SILENCED TOPRE KEYBOARDS. Thank you for understanding!",
    10,
    100.00,
    139.99,
    deskeys
)
product_repository.save(dess)

desr3 = Product(
    "DES-Rings #3 (thin)",
    parts,
    "Custom foam silencing rings to reduce key return noise caused by the sliders on Topre keyboards colliding with the underside of the switch housing when typing. Please be mindful of the effect these will have on key travel and choose an appropriate thickness of silencing ring to suit the sliders in your keyboard. Standard unsilenced Topre has a total key travel distance of 4 mm, so using 0.5 mm DES-Rings or ordinary Topre rings (which are also 0.5 mm thick) will reduce travel on the normal sliders to 3.5 mm, but using the same 0.5 mm rings on either HHKB Type-S sliders or DES-Sliders will give you a net travel distance of 3.8 mm because the sliders are a different shape to partially offset the travel reduction. REALFORCE and Leopold keyboards that come \"silenced\" from the factory use sliders that offset the full 0.5 mm of travel reduction from the silencing rings they use, so the travel distance on those is still the full 4 mm like unsilenced Topre boards. Thicker rings will of course provide a greater degree of noise reduction, but at 0.3 mm thickness, these #3 rings are a good compromise between noise reduction and travel reduction on normal sliders.",
    8,
    20.00,
    29.99,
    deskeys
)
product_repository.save(desr3)

desr5 = Product(
    "DES-Rings #5 (original)",
    parts,
    "Custom foam silencing rings to reduce key return noise caused by the sliders on Topre keyboards colliding with the underside of the switch housing when typing. Please be mindful of the effect these will have on key travel and choose an appropriate thickness of silencing ring to suit the sliders in your keyboard. Standard unsilenced Topre has a total key travel distance of 4 mm, so using 0.5 mm DES-Rings or ordinary Topre rings (which are also 0.5 mm thick) will reduce travel on the normal sliders to 3.5 mm, but using the same 0.5 mm rings on either HHKB Type-S sliders or DES-Sliders will give you a net travel distance of 3.8 mm because the sliders are a different shape to partially offset the travel reduction. REALFORCE and Leopold keyboards that come \"silenced\" from the factory use sliders that offset the full 0.5 mm of travel reduction from the silencing rings they use, so the travel distance on those is still the full 4 mm like unsilenced Topre boards. These #5 rings have the same 0.5 mm thickness as the silencing rings used by manufacturers of Topre keyboards (including Topre, PFU, and Leopold).",
    8,
    20.00,
    29.99,
    deskeys
)
product_repository.save(desr5)

desr7 = Product(
    "DES-Rings #7 (extra silent)",
    parts,
    "Custom foam silencing rings to reduce key return noise caused by the sliders on Topre keyboards colliding with the underside of the switch housing when typing. Please be mindful of the effect these will have on key travel and choose an appropriate thickness of silencing ring to suit the sliders in your keyboard. Standard unsilenced Topre has a total key travel distance of 4 mm, so using 0.5 mm DES-Rings or ordinary Topre rings (which are also 0.5 mm thick) will reduce travel on the normal sliders to 3.5 mm, but using the same 0.5 mm rings on either HHKB Type-S sliders or DES-Sliders will give you a net travel distance of 3.8 mm because the sliders are a different shape to partially offset the travel reduction. REALFORCE and Leopold keyboards that come \"silenced\" from the factory use sliders that offset the full 0.5 mm of travel reduction from the silencing rings they use, so the travel distance on those is still the full 4 mm like unsilenced Topre boards. These #7 rings have a thickness of 0.7 mm, which makes them noticeably more effective at quieting more aggressively tactile  are best used with sliders that take silencing rings into account, such as DES-Sliders or the stock sliders from an already \"silenced\" Topre keyboard.",
    8,
    20.00,
    29.99,
    deskeys
)
product_repository.save(desr7)

desd1c = Product(
    "DES-Domes V1 Carrot rubber domes",
    parts,
    "Custom replacement Topre-compatible rubber domes in strips of 4. Each kit contains 112 domes (28 strips of 4). These Carrot domes target an approximately 60 g actuation force and have a tactile bump somewhere in between the very round bump of standard Topre and the much more binary one of Sony BKE (and Keyclack BKE REDUX) domes and other DES-Domes from the V1 range. Other DES-Domes V1 (and the BKE ones) also have open tops; these, like original Topre domes, do not. If you like stock 55 g Topre domes but would prefer them to be just a hair more abrupt/binary in their tactile response, you might just love these.",
    5,
    62.00,
    74.99,
    deskeys
)
product_repository.save(desd1c)

desd2t = Product(
    "DES-Domes V2 Tiffany rubber domes",
    parts,
    "Custom replacement Topre-compatible rubber domes in strips of 4. Each kit contains 112 domes (28 strips of 4). These feather-light Tiffany domes target an approximately 35 g actuation force and have a tactile bump somewhere in between the very round bump of standard Topre and the much more binary one of Sony BKE (and Keyclack BKE REDUX) domes and most DES-Domes from the V1 range. The majority of DES-Domes V1 also have open tops; these V2s, like original Topre domes, do not. If you like the effortless typing feel of 30 g Topre domes but would prefer a little more tactile feedback, these are a solid choice.",
    5,
    62.00,
    74.99,
    deskeys
)
product_repository.save(desd2t)

desd2p = Product(
    "DES-Domes V2 Purple rubber domes",
    parts,
    "Custom replacement Topre-compatible rubber domes in strips of 4. Each kit contains 112 domes (28 strips of 4). These Purple domes target an approximately 49 g actuation force and have a tactile bump somewhere in between the very round bump of standard Topre and the much more binary one of Sony BKE (and Keyclack BKE REDUX) domes and most DES-Domes from the V1 range. The majority of DES-Domes V1 also have open tops; these V2s, like original Topre domes, do not. If you're a fan of standard 45 g Topre REALFORCE domes but would prefer just a little more tactile feedback, these could be the domes for you.",
    5,
    62.00,
    74.99,
    deskeys
)
product_repository.save(desd2p)

breakpoint()
