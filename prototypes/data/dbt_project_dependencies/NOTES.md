# Hiccup #1 - Project Dependencies Are DBT-Cloud Only

I didn't realise this but DBT project dependencies are, natively, dbt cloud only.
You can't do this locally.

Some rough workarounds I'm playing around with:

- `dbt-loom` - apparently handles this for you. I'm investigating it now.
  - See this: https://github.com/Bl3f/dbt-loom-example
- DBT packages _may_ be able to handle this for you? I need to look into this.
  - For example, you can see this example here: https://github.com/dbt-labs/facebook-ads
  - Another one: https://github.com/dbt-labs/adwords
- Rolling my own code injection/orchestration tooling?

Results?

- The `dbt-loom` approach seems very promising. It is basically what DBT are
  locking behind their paywall.
- It allows us to "select" from upstream models.
- The only question I have is around instances - do all projects select from the
  same "sources"? If so, I will probably need to use dbt packages.

- Quick investigation of using DBT dependencies seems to indicate this is the
  right path forward.
- Each "downstream" repo has to configure, build, and manage their own instance
  of the model via their configured profile.
- In our `dbt_deps_example`, this is the package that would be installed in an
  upstream project.
