DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category_id INT REFERENCES categories(id),
    description TEXT NOT NULL,
    quantity INT NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    manufacturer_id INT REFERENCES manufacturers(id)
);

INSERT INTO categories (name) VALUES ('Keyboards');
INSERT INTO categories (name) VALUES ('Parts');

INSERT INTO manufacturers (name, country) VALUES ('Topre', 'JP');
INSERT INTO manufacturers (name, country) VALUES ('PFU', 'JP');
INSERT INTO manufacturers (name, country) VALUES ('Leopold', 'KR');
INSERT INTO manufacturers (name, country) VALUES ('Deskeys', 'CN');

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'REALFORCE R2SA-US4-IV PFU Limited Edition (ivory)',
    1,
    'High-end 108-key keyboard exclusively manufactured by Topre to PFU''s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer.',
    4,
    180.00,
    216.66,
    1
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'REALFORCE R2SA-US4-BK PFU Limited Edition (black)',
    1,
    'High-end 108-key keyboard exclusively manufactured by Topre to PFU''s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer.',
    4,
    180.00,
    216.66,
    1
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'REALFORCE R2TLSA-US4-IV PFU Limited Edition (ivory)',
    1,
    'High-end 87-key keyboard exclusively manufactured by Topre to PFU''s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer.',
    8,
    180.00,
    216.66,
    1
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'REALFORCE R2TLSA-US4-BK PFU Limited Edition (black)',
    1,
    'High-end 87-key keyboard exclusively manufactured by Topre to PFU''s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer.',
    8,
    180.00,
    216.66,
    1
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Classic PD-KB401W (white, printed keycaps)',
    1,
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    130.00,
    164.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Classic PD-KB401WN (white, blank keycaps)',
    1,
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    130.00,
    164.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Classic PD-KB401B (charcoal, printed keycaps)',
    1,
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    130.00,
    164.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Classic PD-KB401BN (charcoal, blank keycaps)',
    1,
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    130.00,
    164.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid PD-KB800W (white, printed keycaps)',
    1,
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    160.00,
    194.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid PD-KB800WN (white, blank keycaps)',
    1,
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    160.00,
    194.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid PD-KB800B (charcoal, printed keycaps)',
    1,
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    160.00,
    194.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid PD-KB800BN (charcoal, blank keycaps)',
    1,
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    160.00,
    194.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid Type-S PD-KB800WS (white, printed keycaps)',
    1,
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    185.00,
    224.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid Type-S PD-KB800WNS (white, blank keycaps)',
    1,
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features blank keycaps.',
    6,
    185.00,
    224.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid Type-S PD-KB800BS (charcoal, printed keycaps)',
    1,
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    185.00,
    224.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid Type-S PD-KB800BNS (charcoal, blank keycaps)',
    1,
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features blank keycaps.',
    6,
    185.00,
    224.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid Type-S Snow Limited Edition PD-KB800YS (pure white, printed keycaps)',
    1,
    'The exclusive Snow model released for the HHKB''s 25th anniversary is a pure white version of the HYBRID Type-S and includes a limited edition HHKB25 "FN" key, making it a unique piece of HHKB history. Only 250 units made available to the EMEA market area.',
    0,
    200.00,
    239.99,
    2
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'Leopold FC660C (white)',
    1,
    '66-key keyboard manufactured by Leopold. Uses 45 g capacitive Topre key switches.',
    0,
    180.00,
    216.66,
    3
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'Leopold FC660C (black)',
    1,
    '66-key keyboard manufactured by Leopold. Uses 45 g capacitive Topre key switches.',
    0,
    180.00,
    216.66,
    3
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'DES-Sliders',
    2,
    'Custom, Cherry MX keycap compatible replacement sliders for Topre keyboards. Made of Polyoxymethylene (POM) and manufactured within extremely strict tolerances, these are designed to fit more snugly than stock Topre sliders while also exhibiting less friction when actuated. They are also designed to allow enough space on the slider such that 0.5 mm silencing rings will result in a total key travel distance of 3.8 mm, which is the same as a HHKB Type-S (but 0.2 mm less than silenced REALFORCE/Leopold or unsilenced Topre). Each kit contains 102 1u sliders, 7 2u stabiliser-sliders, and 1 set of space bar stabiliser sliders and housings. Use the original stabiliser wires from a Topre keyboard on stabilised keys. IMPORTANT: If using these in any "silenced" Topre keyboard other than a Type-S HHKB, you will need to source replacement housings for keys larger than 1u. This is because silenced Topre keyboards use different housings and sliders for the 2u stabilisers in order to accommodate the 1 mm silencing rings they come with to avoid a reduction in key travel. HHKB Type-S keyboards use 0.5 mm silencing rings on the 2u keys, exactly the same as the ones on the 1u keys, and only the sliders (not the housings as well) are adjusted to partially compensate. Please bear this in mind if you plan to use DES-Sliders in any other silenced Topre keyboard, including REALFORCE and Leopold boards. RETURNS WILL NOT BE ACCEPTED ON THE BASIS OF INCOMPATIBILITY WITH SILENCED TOPRE KEYBOARDS. Thank you for understanding!',
    10,
    100.00,
    139.99,
    4
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'DES-Rings #3 (thin)',
    2,
    'Custom foam silencing rings to reduce key return noise caused by the sliders on Topre keyboards colliding with the underside of the switch housing when typing. Please be mindful of the effect these will have on key travel and choose an appropriate thickness of silencing ring to suit the sliders in your keyboard. Standard unsilenced Topre has a total key travel distance of 4 mm, so using 0.5 mm DES-Rings or ordinary Topre rings (which are also 0.5 mm thick) will reduce travel on the normal sliders to 3.5 mm, but using the same 0.5 mm rings on either HHKB Type-S sliders or DES-Sliders will give you a net travel distance of 3.8 mm because the sliders are a different shape to partially offset the travel reduction. REALFORCE and Leopold keyboards that come "silenced" from the factory use sliders that offset the full 0.5 mm of travel reduction from the silencing rings they use, so the travel distance on those is still the full 4 mm like unsilenced Topre boards. Thicker rings will of course provide a greater degree of noise reduction, but at 0.3 mm thickness, these #3 rings are a good compromise between noise reduction and travel reduction on normal sliders.',
    8,
    20.00,
    29.99,
    4
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'DES-Rings #5 (original)',
    2,
    'Custom foam silencing rings to reduce key return noise caused by the sliders on Topre keyboards colliding with the underside of the switch housing when typing. Please be mindful of the effect these will have on key travel and choose an appropriate thickness of silencing ring to suit the sliders in your keyboard. Standard unsilenced Topre has a total key travel distance of 4 mm, so using 0.5 mm DES-Rings or ordinary Topre rings (which are also 0.5 mm thick) will reduce travel on the normal sliders to 3.5 mm, but using the same 0.5 mm rings on either HHKB Type-S sliders or DES-Sliders will give you a net travel distance of 3.8 mm because the sliders are a different shape to partially offset the travel reduction. REALFORCE and Leopold keyboards that come "silenced" from the factory use sliders that offset the full 0.5 mm of travel reduction from the silencing rings they use, so the travel distance on those is still the full 4 mm like unsilenced Topre boards. These #5 rings have the same 0.5 mm thickness as the silencing rings used by manufacturers of Topre keyboards (including Topre, PFU, and Leopold).',
    8,
    20.00,
    29.99,
    4
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'DES-Rings #7 (extra silent)',
    2,
    'Custom foam silencing rings to reduce key return noise caused by the sliders on Topre keyboards colliding with the underside of the switch housing when typing. Please be mindful of the effect these will have on key travel and choose an appropriate thickness of silencing ring to suit the sliders in your keyboard. Standard unsilenced Topre has a total key travel distance of 4 mm, so using 0.5 mm DES-Rings or ordinary Topre rings (which are also 0.5 mm thick) will reduce travel on the normal sliders to 3.5 mm, but using the same 0.5 mm rings on either HHKB Type-S sliders or DES-Sliders will give you a net travel distance of 3.8 mm because the sliders are a different shape to partially offset the travel reduction. REALFORCE and Leopold keyboards that come "silenced" from the factory use sliders that offset the full 0.5 mm of travel reduction from the silencing rings they use, so the travel distance on those is still the full 4 mm like unsilenced Topre boards. These #7 rings have a thickness of 0.7 mm, which makes them noticeably more effective at quieting more aggressively tactile  are best used with sliders that take silencing rings into account, such as DES-Sliders or the stock sliders from an already "silenced" Topre keyboard.',
    8,
    20.00,
    29.99,
    4
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'DES-Domes V1 Carrot rubber domes',
    2,
    'Custom replacement Topre-compatible rubber domes in strips of 4. Each kit contains 112 domes (28 strips of 4). These Carrot domes target an approximately 60 g actuation force and have a tactile bump somewhere in between the very round bump of standard Topre and the much more binary one of Sony BKE (and Keyclack BKE REDUX) domes and other DES-Domes from the V1 range. Other DES-Domes V1 (and the BKE ones) also have open tops; these, like original Topre domes, do not. If you like stock 55 g Topre domes but would prefer them to be just a hair more abrupt/binary in their tactile response, you might just love these.',
    5,
    62.00,
    74.99,
    4
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'DES-Domes V2 Tiffany rubber domes',
    2,
    'Custom replacement Topre-compatible rubber domes in strips of 4. Each kit contains 112 domes (28 strips of 4). These feather-light Tiffany domes target an approximately 35 g actuation force and have a tactile bump somewhere in between the very round bump of standard Topre and the much more binary one of Sony BKE (and Keyclack BKE REDUX) domes and most DES-Domes from the V1 range. The majority of DES-Domes V1 also have open tops; these V2s, like original Topre domes, do not. If you like the effortless typing feel of 30 g Topre domes but would prefer a little more tactile feedback, these are a solid choice.',
    5,
    62.00,
    74.99,
    4
);

INSERT INTO products (name, category_id, description, quantity, cost, price, manufacturer_id)
VALUES (
    'DES-Domes V2 Purple rubber domes',
    2,
    'Custom replacement Topre-compatible rubber domes in strips of 4. Each kit contains 112 domes (28 strips of 4). These Purple domes target an approximately 49 g actuation force and have a tactile bump somewhere in between the very round bump of standard Topre and the much more binary one of Sony BKE (and Keyclack BKE REDUX) domes and most DES-Domes from the V1 range. The majority of DES-Domes V1 also have open tops; these V2s, like original Topre domes, do not. If you''re a fan of standard 45 g Topre REALFORCE domes but would prefer just a little more tactile feedback, these could be the domes for you.',
    5,
    62.00,
    74.99,
    4
);
