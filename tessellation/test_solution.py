# %%
import numpy as np
import solution


# %%
def is_correct_step_shape(start_point: list[int, int], end_point: list[int, int]) -> bool:
    start_point, end_point = np.array(start_point), np.array(end_point)
    shape = np.abs(start_point - end_point)
    return shape.sum() == 3 and (shape[0] == 1 or shape[1] == 1)


assert is_correct_step_shape([0, 0], [-2, 1])
assert is_correct_step_shape([-2, 1], [0, 0])
assert not is_correct_step_shape([1, 1], [0, 0])


# %%


def is_point_on_desk(point: list[int, int], desk_size: list[int, int]) -> bool:
    point, desk_size = np.array(point), np.array(desk_size)
    return np.all(desk_size > point) and np.all(0 <= point)


assert not is_point_on_desk([1, -1], [2, 1])
assert is_point_on_desk([0, 0], [1, 1])
assert not is_point_on_desk([1, 0], [1, 1])


# %%
def fill_desk(points: list[list[int, int]], desk_size: list[int, int]) -> np.array:
    points = np.array(points)
    desk = np.zeros(desk_size)
    indexes = points[:, 0] * desk_size[1] + points[:, 1]
    desk.flat[indexes] = 1
    return desk


def is_desk_tessellated(points: list[list[int, int]], desk_size: list[int, int]) -> bool:
    desk = fill_desk(points, desk_size)
    return desk.sum() == desk_size[0] * desk_size[1]


assert not is_desk_tessellated([[0, 0], [1, 0], [2, 1], [0, 1], [1, 1], [2, 0]], [3, 3])
assert is_desk_tessellated([[0, 0], [1, 0], [2, 1], [0, 1], [1, 1], [2, 0]], [3, 2])


# %%

# %%
def evaluate_task(desk_size, solver):
    print(f"{desk_size=}")
    points = solver(desk_size)
    if not points:
        error_msg = f"empty solution"
        raise Exception(error_msg)
    else:
        print("empty test is passed")

    out_points = {index: point for index, point in enumerate(points) if not is_point_on_desk(point, desk_size)}
    if out_points:
        error_msg = f"points out of desk were found"
        for point_index, point in out_points.items():
            error_msg += f"\n{point_index=} {point=}"
        raise Exception(error_msg)
    else:
        print("out points test is passed")

    incorrect_steps = {
        index: (start_point, end_point)
        for index, (start_point, end_point) in enumerate(zip(points, points[1:]))
        if not is_correct_step_shape(start_point, end_point)
    }
    if incorrect_steps:
        error_msg = f"incorrect steps were found"
        for step_index, (start_point, end_point) in incorrect_steps.items():
            error_msg += f"\n{step_index=} {start_point=} {end_point=}"
        raise Exception(error_msg)
    else:
        print("incorrect steps test is passed")

    desk = fill_desk(points, desk_size)
    if not is_desk_tessellated(points, desk_size):
        error_msg = f"tessellation is not complete"
        error_msg += f"\n{desk=}"
        raise Exception(error_msg)
    else:
        print("tessellation test is passed")

    score = desk.sum() / len(points)
    return score


if __name__ == "__main__":
    desk_sizes = [list(np.random.randint(5, high, size=2)) for high in list(range(10, 110)) * 1]
    scores = [evaluate_task(desk_size, solution.main) for desk_size in desk_sizes]
    print(f"{np.mean(scores)=}, {np.std(scores)=}, {len(scores)=}")
