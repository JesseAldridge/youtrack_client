import easygraph

with open('youtrack_tracker.log') as f:
    text = f.read()
counts = [int(x) for x in text.splitlines()]
easygraph.graph(zip(range(len(counts)), counts), show_lines=True)
