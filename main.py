import os
from random import randint
from typing import Callable
from timeit import default_timer
from sorts import bubble_sort, selection_sort, quick_sort
from utils import Number
from student import Student, Grades

CHUNK: int = 25_000 // 3

rev: list[Number] = list(reversed(list(range(CHUNK))))
repeat: list[Number] = [CHUNK for _ in range(CHUNK)]
even: list[Number] = [int(i / 2) if i % 2 == 0 else i for i in range(CHUNK)]

unsorted_list: list[Number] = rev + repeat + even


def try_sorting(
    name: str,
    sorting_fn: Callable[[list[Number]], list[Number]],
    max_line_length: int = 140,
) -> str:
    start_time = default_timer()
    after_sorting = sorting_fn(unsorted_list)

    name_column: str = name.center(max_line_length, "-")
    time_took: str = f"Time took: {default_timer() - start_time:.6f} seconds"
    array_size: str = f"Size of array: {len(unsorted_list)}"
    sorted_elements: str = (
        f"Sorted elements: {', '.join([str(x) for x in after_sorting[:10]])}..."
    )
    content: str = f"{time_took} | {array_size} | {sorted_elements}".center(
        max_line_length
    )
    dashed: str = "-" * max_line_length

    for i in range(len(after_sorting) - 2):
        assert after_sorting[i] <= after_sorting[i + 1]

    return f"{name_column}\n" f"{content}\n" f"{dashed}\n\n"


def try_bubble_sort():
    return try_sorting(name="Bubble sort", sorting_fn=bubble_sort)


def try_selection_sort():
    return try_sorting(
        name="Selection sort",
        sorting_fn=selection_sort,
    )


def try_quick_sort():
    return try_sorting(
        name="Quick sort",
        sorting_fn=quick_sort,
    )


if __name__ == "__main__":
    os.system("cls")

    try:
        with open("sorts_output.txt", "w", encoding="UTF-8") as f:
            try:
                # f.write(try_bubble_sort())
                # f.write(try_selection_sort())
                f.write(try_quick_sort())
            except (IOError, OSError) as e:
                print(f"Error writing to file: {e}")
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"Error opening file: {e}")

    for student in [
        Student(**info)
        for info in [
            {
                "surname": f"Surname{randint(0, 1000)}",
                "name": f"Name{randint(0, 1000)}",
                "patronymic": f"Patronymic{randint(0, 1000)}",
                "grades": Grades.generate_random_grades(),
            }
            for _ in range(5)
        ]
    ]:
        print(student)
