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


def get_result_2(workflows, parts):
    pass


def main():
    workflows, parts = load_data("data.txt")
    print(get_result(workflows, parts))
    print(get_result_2(workflows, parts))


if __name__ == '__main__':
    main()
