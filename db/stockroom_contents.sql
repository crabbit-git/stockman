DELETE FROM manufacturers;
DELETE FROM products;

INSERT INTO manufacturers (name, country) VALUES ('Topre', 'JP');
INSERT INTO manufacturers (name, country) VALUES ('PFU', 'JP');
INSERT INTO manufacturers (name, country) VALUES ('Leopold', 'KR');

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'REALFORCE R2SA-US4-IV (PFU Limited Edition, ivory)',
    'High-end 108-key keyboard exclusively manufactured by Topre to PFU''s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer.',
    4,
    180.00,
    216.66,
    1
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'REALFORCE R2SA-US4-BK (PFU Limited Edition, black)',
    'High-end 108-key keyboard exclusively manufactured by Topre to PFU''s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer.',
    4,
    180.00,
    216.66,
    1
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'REALFORCE R2TLSA-US4-IV (PFU Limited Edition, ivory)',
    'High-end 87-key keyboard exclusively manufactured by Topre to PFU''s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer.',
    8,
    180.00,
    216.66,
    1
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'REALFORCE R2TLSA-US4-BK (PFU Limited Edition, black)',
    'High-end 87-key keyboard exclusively manufactured by Topre to PFU''s specification. Uses silenced, 45 g capacitive Topre key switches and features configurable Actuation Point Changer.',
    8,
    180.00,
    216.66,
    1
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Classic PD-KB401W (white, printed keycaps)',
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    130.00,
    164.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Classic PD-KB401WN (white, blank keycaps)',
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    130.00,
    164.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Classic PD-KB401B (charcoal, printed keycaps)',
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    130.00,
    164.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Classic PD-KB401BN (charcoal, blank keycaps)',
    'The original wired Happy Hacking Keyboard design, updated and carefully refined for a classic HHKB experience. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    130.00,
    164.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid PD-KB800W (white, printed keycaps)',
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    160.00,
    194.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid PD-KB800WN (white, blank keycaps)',
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    160.00,
    194.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid PD-KB800B (charcoal, printed keycaps)',
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    160.00,
    194.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid PD-KB800BN (charcoal, blank keycaps)',
    'Augmented with Bluetooth, Keymapping and USB-C, so you can experience HHKB on all your modern devices. Uses 45 g capacitive Topre key switches with 4 mm of key travel. This version features blank keycaps.',
    6,
    160.00,
    194.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid Type-S PD-KB800WS (white, printed keycaps)',
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    185.00,
    224.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid Type-S PD-KB800WNS (white, blank keycaps)',
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features blank keycaps.',
    6,
    185.00,
    224.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid Type-S PD-KB800BS (charcoal, printed keycaps)',
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features dye-sublimated keycap legends.',
    6,
    185.00,
    224.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'HHKB Professional Hybrid Type-S PD-KB800BNS (charcoal, blank keycaps)',
    'Hybrid connectivity options and silent key switches for a quieter HHKB experience on all your modern devices. Uses silenced 45 g capacitive Topre key switches with 3.8 mm of key travel. This version features blank keycaps.',
    6,
    185.00,
    224.99,
    2
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'Leopold FC660C (white)',
    '66-key keyboard manufactured by Leopold. Uses 45 g capacitive Topre key switches.',
    0,
    180.00,
    216.66,
    3
);

INSERT INTO products (name, description, quantity, cost, price, manufacturer_id)
VALUES (
    'Leopold FC660C (black)',
    '66-key keyboard manufactured by Leopold. Uses 45 g capacitive Topre key switches.',
    0,
    180.00,
    216.66,
    3
);
