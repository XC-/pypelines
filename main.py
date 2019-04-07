class Phase:
    __valid_condition_types = ["pre", "post"]

    def __init__(self):
        self.conditions = {
            "pre": [],
            "post": []
        }
        self.context = {}

    def add_condition(self, condition_type, function):
        if condition_type not in Phase.__valid_condition_types:
            raise ValueError("Condition type must be 'pre' or 'post'.")
        if not callable(function):
            raise TypeError("Condition must be callable.")
        if function not in self.conditions[condition_type]:
            self.conditions[condition_type].append(function)
        return self.conditions[condition_type]

    def add_pre_condition(self, function):
        return self.add_condition("pre", function)

    def add_post_condition(self, function):
        return self.add_condition("post", function)

    def check_conditions(self, condition_type):
        if condition_type not in Phase.__valid_condition_types:
            raise ValueError("Condition type must be 'pre' or 'post'.")
        return all(c() for c in self.conditions[condition_type])

    def check_pre_conditions(self):
        return self.check_conditions("pre")

    def check_post_conditions(self):
        return self.check_conditions("post")


class Pipeline(Phase):
    def __init__(self):
        self.phases = []
        super().__init__(self)


class Job(Phase):
    def __init__(self):
        super().__init__(self)


def Condition(f):

