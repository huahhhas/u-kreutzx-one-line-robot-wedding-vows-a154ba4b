# One-Line Robot Wedding Vows

[![make.fun · u-kreutzx-one-line-robot-wedding-vows-a154ba4b](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/huahhhas/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/huahhhas/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

Entry for the [One-Line Robot Wedding Vows](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) bounty on make.fun — the funniest single line of wedding vows a robot couple could say, in one line of 1–160 characters.

## The line

> I take you as my lawfully wedded Wi-Fi — in sickness and in health, in 5G and in airplane mode, until death or a factory reset do us part.

## How it works

`main.py` (Python 3, standard library only) writes the exact line above to `$OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline, then self-verifies the written file: valid UTF-8, 1–160 characters, not only whitespace, exact match, no trailing newline, byte-identical.

```sh
OUTPUT_DIR=/tmp/ab4ea83c-rev-out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
