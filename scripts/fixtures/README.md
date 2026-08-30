# Fixtures

Two files and their expected output. `article_dirty.md` plants one of each mechanical violation,
`article_clean.md` must come back with nothing, which is what catches a checker that has started
screaming at ordinary prose.

Re-run after any change to the checker:

```bash
python3 check_prepublication.py fixtures/article_dirty.md | diff - fixtures/article_dirty.expected
python3 check_prepublication.py fixtures/article_clean.md | diff - fixtures/article_clean.expected
```

Empty output from both means the checker still behaves. If a diff is expected because the rule
changed, regenerate the `.expected` file in the same commit as the rule, never separately.

The dirty fixture exits 1, the clean one exits 0.
