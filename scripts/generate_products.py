#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_products.py
Generates a products.json file with fake daily-care product entries (Arabic names).
Usage:
  python3 scripts/generate_products.py [count] [output_file]
Examples:
  python3 scripts/generate_products.py        # generates 10000 items to products.json
  python3 scripts/generate_products.py 5000   # generates 5000 items to products.json
  python3 scripts/generate_products.py 10000 output.json

The data is fictional and intended for testing only.
"""

import json
import random
import sys
from datetime import datetime

# Configuration
DEFAULT_COUNT = 10000
BASE_ID = 1786850025000

categories = [
    "شامبو",
    "بلسم",
    "زيت للشعر",
    "كريم مرطب",
    "منظف وجه",
    "مزيل عرق",
    "معجون أسنان",
    "كريم لليدين",
    "سيروم",
    "غسول",
    "تونر",
    "ماسك",
    "مناديل مبللة",
    "مزيل مكياج",
    "لوشن للجسم",
    "سبراي للشعر",
    "جل استحمام",
    "شامبو للأطفال",
    "كريم للشعر",
    "مقشر"
]

adjectives = [
    "الترطيب اليومي",
    "المغذي",
    "المنعش",
    "الخفيف",
    "الخالٍ من العطور",
    "للبشرة الحساسة",
    "بتقنية متقدمة",
    "بتركيبة طبيعية",
    "بتركيز عالي",
    "مناسب للجميع"
]

sizes = ["30 مل", "50 مل", "75 مل", "100 مل", "150 مل", "200 مل"]


def generate_item(index):
    pid = BASE_ID + index
    category = random.choice(categories)
    adj = random.choice(adjectives)
    size = random.choice(sizes)
    name = f"{category} {adj} {size}"
    # deterministic-ish price but with randomness for variety
    price = round(random.uniform(1.00, 99.99), 2)
    image = f"https://picsum.photos/seed/{pid}/400/400"
    return {"id": pid, "name": name, "price": price, "image": image}


def main():
    count = DEFAULT_COUNT
    out_file = "products.json"
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            pass
    if len(sys.argv) > 2:
        out_file = sys.argv[2]

    random.seed(42)  # reproducible output
    products = [generate_item(i) for i in range(count)]

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f"Generated {count} fictional products to '{out_file}' at {datetime.utcnow().isoformat()}Z")


if __name__ == "__main__":
    main()
