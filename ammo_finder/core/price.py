def extract_price(data : str) -> int:
    trimmed = data.strip()\
        .replace(",-", "")\
        .replace(" ", "")\
        .replace("Fra", "")\
        .replace("fra", "")\
        .replace(",", ".")

    return float(trimmed)

