def pipeline(value, *functions, **settings):
    repeat = settings.get("repeat", 1)
    debug = settings.get("debug", False)
    stop_condition = settings.get("stop_condition")

    current = value

    for r in range(repeat):
        if debug:
            print(f"\nПовтор {r + 1}")

        for i, func in enumerate(functions, start=1):
            current = func(current)

            if debug:
                print(f"  Шаг {i}: {current}")

            if stop_condition and stop_condition(current):
                if debug:
                    print("Условие остановки выполнено")
                return current

    return current
