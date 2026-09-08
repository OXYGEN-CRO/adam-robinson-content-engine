# Credentials and private configuration

Store authentication in the connected application's OAuth or CLI credential
store. Keep local preferences and workspace IDs in ignored
`workspace.local.json` and `strategy/notion.local.json`. Start from the blank
example files. Public Notion template URLs identify a template, not a write
destination for a clone.

Do not commit API keys, bearer tokens, private keys, session cookies, signed
download URLs, private customer records or credential-bearing debug logs.
`.gitignore` is a convenience, not a security scan; already tracked files and
previous commits remain visible in Git history.

Before a public release, install [Gitleaks](https://github.com/gitleaks/gitleaks)
and run:

```sh
gitleaks dir --redact .
gitleaks git --redact --log-opts='--all' .
./scripts/wiki-lint.sh
```

Review findings rather than excluding entire source archives. Any necessary
exception must identify the exact non-secret finding. If a real credential is
found, revoke or rotate it through its provider before removing it from all
public refs. Do not paste the credential into a public issue.

Use GitHub's **Security → Report a vulnerability** on the public repository
for private reports. Include the affected path and commit, with secret values
redacted.
