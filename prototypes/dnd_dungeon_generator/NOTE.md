# Better Mapping Framework

How can I better, more elegantly expressed associations? e.g. can each one line
associate some "keys" to some "values".

e.g.

```
...
location:mine & history:(active|abandoned) -> monster:goblin
location:(mine|cave) & history:abandoned -> monster:spider
location:* & history:haunted -> monster:ghost
...
```

This could express lots of individual configurations which can chain together
into a more complex procedure.
