# AMIE Rule Wrapper

A wrapper which wraps **AMIE+** rules into a more intuitive data structure.

## Python Files

### amie\_rule\_wrapper.py

This module contains classes which allow to wrap rules from **AMIE+** standard output into an object oriented data structure.

Example usage:

```python
from amie_rule_wrapper import AMIERule, NoAMIERuleInLineError

amie_rules = set()

with open(amie_output_fn, "r") as f:
    lines = f.readlines()
    for line in lines:
        try:
            amie_rule = AMIERule(line)
            amie_rules.add(amie_rule)
        except NoAMIERuleInLineError:
            continue
```

