class State:
    def __init__(self, rule, dot_index, start_index):
        self.rule = rule
        self.dot_index = dot_index
        self.start_index = start_index

    def __eq__(self, other):
        return self.rule == other.rule and self.dot_index == other.dot_index and self.start_index == other.start_index

    def __hash__(self):
        return hash((self.rule, self.dot_index, self.start_index))

    def __str__(self):
        return f'{self.rule} : {"".join(self.rule)} - {self.dot_index} - {self.start_index}'

def earley_parse(grammar, sentence):
    chart = [[] for _ in range(len(sentence) + 1)]
    start_rule = next(iter(grammar))
    start_state = State(start_rule, 0, 0)
    chart[0].append(start_state)

    for i in range(len(sentence) + 1):
        while True:
            added = False
            for state in chart[i]:
                if state.dot_index < len(state.rule) and state.rule[state.dot_index] in grammar:
                    non_terminal = state.rule[state.dot_index]
                    for rule in grammar[non_terminal]:
                        new_state = State(rule, 0, i)
                        if new_state not in chart[i]:
                            chart[i].append(new_state)
                            added = True

                elif state.dot_index < len(state.rule) and state.rule[state.dot_index] == sentence[i - 1]:
                    new_state = State(state.rule, state.dot_index + 1, state.start_index)
                    if new_state not in chart[i]:
                        chart[i].append(new_state)
                        added = True

                elif state.dot_index == len(state.rule):
                    for s in chart[state.start_index]:
                        if s.dot_index < len(s.rule) and s.rule[s.dot_index] == state.rule[0]:
                            new_state = State(s.rule, s.dot_index + 1, s.start_index)
                            if new_state not in chart[i]:
                                chart[i].append(new_state)
                                added = True

            if not added:
                break

    for i in range(len(chart)):
        print(f"Chart[{i}]:")
        for state in chart[i]:
            print(state)
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['DET', 'N'], ['N']],
    'VP': [['V', 'NP']],
    'DET': ['the', 'a'],
    'N': ['man', 'ball', 'woman', 'table'],
    'V': ['hit', 'took', 'saw', 'liked']
}

sentence = ['the', 'man', 'hit', 'the', 'table']

earley_parse(grammar, sentence)
