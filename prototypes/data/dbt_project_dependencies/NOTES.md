# Hiccup #1 - Project Dependencies Are DBT-Cloud Only

I didn't realise this but DBT project dependencies are, natively, dbt cloud only.
You can't do this locally.

Some rough workarounds I'm playing around with:
- `dbt-loom` - apparently handles this for you. I'm investigating it now.
- Rolling my own code injection/orchestration tooling?