class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        seen = {}
        day = 0
        while day < n:
            state = tuple(cells)

            if state in seen:
                cycle = day - seen[state]
                remaining_day = (n - day) % cycle

                target_day = day + remaining_day - cycle

                for pattern,prev_day in seen.items():
                    if prev_day == target_day:
                        return list(pattern)

            else:
                seen[state] = day

            new_cells = [0] * 8

            for i in  range(1,7):
                new_cells[i] = int(cells[i-1] == cells[i+1])
            
            cells = new_cells
            day += 1
        return cells