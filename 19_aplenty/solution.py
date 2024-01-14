import re


class Part:
    def __init__(self, line: str):
        self.ratings = self._parse(line)

    def _parse(self, line: str):
        xmas = re.findall(r"[0-9]+", line)
        keys = ["x", "m", "a", "s"]
        return {key: int(value) for key, value in zip(keys, xmas)}

    def rate(self, workflows):
        result = "in"
        while not result in ["A", "R"]:
            result = workflows[result].evaluate(self)
        if result == "R":
            return 0
        return sum(self.ratings.values())


class PartRange:
    def __init__(self, workflow_id, xmas: dict[str, tuple[int, int]]):
        self.workflow_id = workflow_id
        self.xmas = xmas

    def combinations(self):
        product = 1
        for x in self.xmas.values():
            product *= (x[1] - x[0])
        return product


class Rule:
    def __init__(self, rule_string):
        self._condition , self._return = self._parse(rule_string)

    def _parse(self, rule_string: str):
        if ":" in rule_string:
            condition, return_ = rule_string.split(":")
        else:
            condition, return_ = ("x>-1", rule_string)
        category = condition[0]
        operator = condition[1]
        number = int(condition[2:])
        return (category, operator, number), return_

    def evaluate(self, part: Part) -> str:
        category, operator, number  = self._condition
        if operator == ">":
            if part.ratings[category] > number:
                return self._return
        if operator == "<":
            if part.ratings[category] < number:
                return self._return
        return ""

    def split(self, part_range: PartRange) -> tuple[PartRange, PartRange]:
        category, operator, number  = self._condition
        if operator == ">":
            xmas = part_range.xmas
            xmas[category] = (number + 1, xmas[category][1])
            accepted_range = PartRange(self._return, xmas)
            xmas = part_range.xmas
            xmas[category] = (xmas[category][0], number)
            rejected_range = PartRange("", xmas)
        else:
            xmas = part_range.xmas
            xmas[category] = (xmas[category][0], number - 1)
            accepted_range = PartRange(self._return, xmas)
            xmas = part_range.xmas
            xmas[category] = (number, xmas[category][1])
            rejected_range = PartRange("", xmas)
        return accepted_range, rejected_range


class Workflow:
    def __init__(self, line):
        self.rules = self._parse(line)

    def _parse(self, line: str) -> list[Rule]:
        rule_strings = line.split(",")
        return [Rule(rule) for rule in rule_strings]

    def evaluate(self, part: Part) -> str:
        for rule in self.rules:
            result = rule.evaluate(part)
            if rule.evaluate(part) != "":
                return result

    def split(self, part_range: PartRange) -> list[PartRange]:
        new_ranges = []
        next_range = part_range
        for rule in self.rules:
            accepted_range, next_range = rule.split(next_range)
            new_ranges.append(accepted_range)
        return new_ranges


class RangeAnalyzer:
    def __init__(self, workflows: list[Workflow]):
        self._workflows = workflows
        self._part_range_queue = [PartRange("in", {"x": (1, 4000), "m": (1, 4000),"a": (1, 4000),"s": (1, 4000)})]

    def evaluate(self):
        n_combinations = 0
        while self._part_range_queue:
            part_range = self._part_range_queue.pop(-1)
            new_ranges = self._workflows[part_range.workflow_id].split(part_range)
            for new_range in new_ranges:
                if new_range.workflow_id == "R":
                    continue
                elif new_range.workflow_id == "A":
                    n_combinations += new_range.combinations()
                else:
                    self._part_range_queue.append(new_range)
        return n_combinations


def load_data(filename):
    workflows = {}
    parts = []
    workflows_read = False
    with open(filename, "r") as file:
        for line in file:
            if line == "\n":
                line = file.readline()
                workflows_read = True
            if not workflows_read:
                name, rules = line.strip().split("{")
                workflows[name] = Workflow(rules[:-1])
            else:
                parts.append(Part(line[1:-1]))
    for part in parts:
        print(part.ratings)
    return workflows, parts


def get_result(workflows, parts):
    return sum([part.rate(workflows) for part in parts])


def get_result_2(workflows):
    return RangeAnalyzer(workflows).evaluate()


def main():
    workflows, parts = load_data("data.txt")
    print(get_result(workflows, parts))
    print(get_result_2(workflows))


if __name__ == '__main__':
    main()
