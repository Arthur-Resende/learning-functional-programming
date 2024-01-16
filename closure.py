def counter():
    count = 0

    def current_count():
        return count

    def increment():
        nonlocal count
        count += 1

    return {
        'current': current_count,
        'increment': increment
    }


# Example usage:
counter_instance = counter()
print(counter_instance["current"]())  # Should print 0
counter_instance["increment"]()
print(counter_instance["current"]())  # Should print 1
counter_instance["increment"]()
print(counter_instance["current"]())  # Should print 2