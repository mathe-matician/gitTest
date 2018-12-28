dest = set(flights2.values())

when = {thing: [k for k, v in flights2.items() if v == thing]
        for thing in dest}
