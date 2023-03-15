def oxford_comma(items):
    if len(items) == 1:
        return str(items[0])
    elif len(items) == 2:
        return (f"{items[0]} and {items[1]}")
    else:
        oxford_items = [str(item) for item in items[:-1]]
        oxford_items.append(f"and {items[-1]}")
        return ", ".join(oxford_items)
