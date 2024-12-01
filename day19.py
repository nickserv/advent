def parse_result(string: str):
    match string:
        case "A":
            return True
        case "R":
            return False
        case _:
            return string


class Rule:
    def __init__(self, category: str, direction: bool, limit: int, result: str | bool):
        self.category = category
        self.direction = direction
        self.limit = limit
        self.result = result

    def __repr__(self):
        return f"Rule({self.category}, {self.direction}, {self.limit}, {self.result})"

    def valid(self, part: dict[str, int]):
        if self.direction:
            if part[self.category] > self.limit:
                return self.result
        if part[self.category] < self.limit:
            return self.result
        return None

    @staticmethod
    def parse(string: str):
        return Rule(
            string[0],
            string[1] == ">",
            int(string[2 : string.index(":")]),
            parse_result(string[string.index(":") + 1 :]),
        )


class Workflow:
    def __init__(self, rules: list[Rule], default_result: str | bool):
        self.rules = rules
        self.default_result = default_result

    def __repr__(self):
        return f"Workflow({self.rules}, {self.default_result})"

    def valid(self, part: dict[str, int]):
        for rule in self.rules:
            result = rule.valid(part)
            if result:
                return result
        return self.default_result

    @staticmethod
    def parse(string: str):
        return Workflow(
            list(map(Rule.parse, string.split(",")[:-1])),
            parse_result(string.split(",")[-1]),
        )


def parse_workflows(string: str):
    return dict(
        (line[: line.index("{")], Workflow.parse(line[line.index("{") + 1 : -1]))
        for line in string.splitlines()
    )


def parse_part(string: str):
    part: dict[str, int] = {}
    for substring in string[1:-1].split(","):
        category, value = substring.split("=")
        part[category] = int(value)
    return part


def valid(workflows: dict[str, Workflow], part: dict[str, int]):
    workflow = "in"
    while not isinstance(workflow, bool):
        workflow = workflows[workflow].valid(part)
    return workflow


def sum_valid(workflows: dict[str, Workflow], parts: list[dict[str, int]]):
    return sum(sum(part.values()) for part in parts if valid(workflows, part))
