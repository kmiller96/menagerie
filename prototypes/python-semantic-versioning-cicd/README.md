# Python SemVer CI/CD

Showcase how you can semantically bump a python package version in Github using
Github Actions.

On commit to `main`, this would:

1. Clone the repo.
2. Run the `bump2version patch` command.
3. Commit these new version numbers.
4. Push this commit to the `main` branch.