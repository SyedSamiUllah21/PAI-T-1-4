def water_jug_dfs(CAP_A, CAP_B, TARGET):
    start_state = (0, 0)
    path = []
    visited = set()
    def dfs(current_state):
        a, b = current_state
        path.append(current_state)
        visited.add(current_state)
        if a == TARGET or b == TARGET:
            print("Solution found!")
            print("Sequence of states leading to the solution:")
            for (x, y) in path:
                print(f"({x}, {y})")
            print()
            return True
        next_states = []
        next_states.append((CAP_A, b))
        next_states.append((a, CAP_B))
        next_states.append((0, b))
        next_states.append((a, 0))
        pour_amount = min(a, CAP_B - b)
        new_a = a - pour_amount
        new_b = b + pour_amount
        next_states.append((new_a, new_b))
        pour_amount = min(b, CAP_A - a)
        new_b = b - pour_amount
        new_a = a + pour_amount
        next_states.append((new_a, new_b))
        for state in next_states:
            if state not in visited:
                if dfs(state):
                    return True
        path.pop()
        return False
    found_solution = dfs(start_state)
    if not found_solution:
        print(f"No solution found for measuring exactly {TARGET} liters with jugs of capacity {CAP_A} and {CAP_B}.")

print("Running Water Jug DFS with jug capacities 4 and 3, aiming for 2 liters:")
water_jug_dfs(4, 3, 2)
