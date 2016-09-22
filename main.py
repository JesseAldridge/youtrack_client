#!/usr/bin/python
import os

import pull_tech_debt, parse_tech_debt, pull_and_post_daily_tickets

pull_tech_debt.pull_tech_debt()
print parse_tech_debt.parse_tech_debt()
os.remove(os.path.expanduser('~/Desktop/out.json'))

pull_and_post_daily_tickets.pull_and_post_daily_tickets()
