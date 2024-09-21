"""Day 19: Aplenty

https://adventofcode.com/2023/day/19

"""
import operator
import re
from dataclasses import dataclass
from typing import Callable


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    def part_sum(self):
        return self.x + self.m + self.a + self.s


@dataclass
class Rule:
    fun: Callable | None
    param: str | None
    result: str
    val: int | None

    def can_apply(self, part):
        if self.param is None:
            return True
        return self.fun(
            getattr(part, self.param),
            self.val
        )


@dataclass
class Workflow:
    name: str
    rules: list[Rule]

    def apply(self, part):
        for r in self.rules:
            if r.can_apply(part):
                return r.result


def parts(data):
    parts_str = data.strip().split('\n\n')[1]
    for part in parts_str.split('\n'):
        yield Part(
            *map(
                int,
                re.findall(
                    r'\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}',
                    part
                )[0]
            )
        )


def parse_rule(rule_str):
    if ':' not in rule_str:  # Terminal rule
        return Rule(None, None, rule_str, None)

    result = rule_str.split(':')[1]
    param = rule_str[0]
    n = int(re.findall(r'(\d+)', rule_str)[0])
    fun = operator.lt if '<' in rule_str else operator.gt

    return Rule(fun, param, result, n)


def parse_workflow(workflow_str):
    name = workflow_str.split('{')[0]
    rules_str = workflow_str.split('{')[1].replace('}', '')
    rules = [parse_rule(rule) for rule in rules_str.split(',')]
    return Workflow(name, rules)


def parse_workflows(data):
    workflows = {}
    workflows_str = data.strip().split('\n\n')[0]
    for workflow_str in workflows_str.split('\n'):
        workflow = parse_workflow(workflow_str)
        workflows[workflow.name] = workflow
    return workflows


def solve_part(part, workflows):
    action = 'in'
    while action not in 'AR':
        action = workflows[action].apply(part)
    if action == 'A':
        return part


def solve(data):
    accepted = []
    workflows = parse_workflows(data)
    for part in parts(data):
        part_result = solve_part(part, workflows)
        if part_result is not None:
            accepted.append(part.part_sum())
    return sum(accepted)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
