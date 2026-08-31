# Fixtures

Three files and their expected output. `article_dirty.md` plants one of each mechanical violation,
`article_substack_dirty.md` carries the raw markdown a Substack production file must not keep, and
`article_clean.md` must come back with nothing, which is what catches a checker that has started
screaming at ordinary prose.

Re-run after any change to the checker:

```bash
for f in article_dirty article_clean article_substack_dirty; do
  python3 check_prepublication.py fixtures/$f.md | diff - fixtures/$f.expected
done
```

Empty output from both means the checker still behaves. If a diff is expected because the rule
changed, regenerate the `.expected` file in the same commit as the rule, never separately.

The two dirty fixtures exit 1, the clean one exits 0.
