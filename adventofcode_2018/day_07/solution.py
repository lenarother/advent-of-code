"""Day 7: The Sum of Its Parts

https://adventofcode.com/2018/day/7

"""
import re
from collections import defaultdict
from itertools import chain
from queue import PriorityQueue
from string import ascii_uppercase

PATTERN = re.compile(
    r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.'
)


def parse_data(data):
    dependency_dict = defaultdict(list)
    for new_dependency, step in re.findall(PATTERN, data):
        dependency_dict[step].append(new_dependency)
    return dependency_dict


def find_root_dependencies(dependencies_dict):
    """Find dependency that has no other dependencies."""
    must_be_finished = set(dependencies_dict.keys())
    can_begin = set(chain(*dependencies_dict.values()))
    return can_begin - must_be_finished


def get_next_steps(dependencies_dict, done_dependencies):
    return [
        step for step, dependencies in dependencies_dict.items()
        if len(set(dependencies) - done_dependencies) == 0
    ]


def solve(data):
    dependency_dict = parse_data(data)

    possible_steps = PriorityQueue()
    for step in find_root_dependencies(dependency_dict):
        possible_steps.put(step)

    first_step = possible_steps.get()
    steps_order = first_step
    done_steps = {first_step}

    while len(dependency_dict) > 0:
        next_steps = get_next_steps(dependency_dict, done_steps)
        for step in next_steps:
            possible_steps.put(step)
            dependency_dict.pop(step)

        next_step = possible_steps.get()
        steps_order += next_step
        done_steps.add(next_step)

    while not possible_steps.empty():
        steps_order += possible_steps.get()

    return steps_order


# Part 2


class StepQueue:

    def __init__(self, data, initial_time=60):
        self.dependency_dict = self.parse_data(data)
        self.todo = PriorityQueue()
        self.done = set()
        self.initial_time = initial_time
        self.find_root_dependencies()

    @staticmethod
    def parse_data(data):
        dependency_dict = defaultdict(list)
        for new_dependency, step in re.findall(PATTERN, data):
            dependency_dict[step].append(new_dependency)
        return dependency_dict

    def find_root_dependencies(self):
        """Find dependency that has no other dependencies."""
        must_be_finished = set(self.dependency_dict.keys())
        can_begin = set(chain(*self.dependency_dict.values()))
        for step in can_begin - must_be_finished:
            self.todo.put(step)

    def update(self):
        available = []
        for step, dependencies in self.dependency_dict.items():
            if len(set(dependencies) - self.done) == 0:
                available.append(step)
        for step in available:
            self.todo.put(step)
            self.dependency_dict.pop(step)

    def get_work(self):
        if self.todo.empty():
            return None, None
        work = self.todo.get()
        work_time = self.initial_time + ascii_uppercase.index(work) + 1
        return work, work_time

    def complete_work(self, work):
        self.done.add(work)

    @property
    def is_empty(self):
        return self.todo.empty() and len(self.dependency_dict) == 0


class Worker:

    def __init__(self, steps_queue):
        self.steps_queue = steps_queue
        self.current_task = None
        self.current_time = None

    @property
    def is_ready(self):
        return self.current_task is None and self.current_time is None

    def work(self):
        if self.is_ready:
            self.current_task, self.current_time = self.steps_queue.get_work()
        if self.current_time:
            self.current_time -= 1
        if self.current_time == 0:
            completed_task = self.current_task
            self.steps_queue.complete_work(completed_task)
            self.current_task = None
            self.current_time = None
            return completed_task


def create_workers(n, steps_queue):
    return [Worker(steps_queue) for _ in range(n)]


def solve2(data, workers_n=5, initial_time=60):
    step_queue = StepQueue(data, initial_time=initial_time)
    workers = create_workers(workers_n, step_queue)
    duration = 0
    while not step_queue.is_empty or not all([w.is_ready for w in workers]):
        for w in workers:
            w.work()
        step_queue.update()
        duration += 1
    return duration


if __name__ == '__main__':
    input_data = open('input_data.txt').read().strip()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read().strip()
    result = solve2(input_data)
    print(f'Example1: {result}')
