class Job:
    def __init__(self, id: int, time: int):
        self.id = id
        self.time = time
        self.conflicts = None
        self.machine = None

    def set_conflicts(self, conflicts):
        relevant_conf = []

        for j in range(len(conflicts)):
            if self.id in conflicts[j]:
                relevant_conf.append(conflicts[j])

        self.conflicts = relevant_conf

    def __repr__(self) -> str:
        return f'Job({repr(self.id)}, {repr(self.time)})'

    def __str__(self) -> str:
        return f'Job({repr(self.id)}, {repr(self.time)})'
