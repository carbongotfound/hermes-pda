# hermes-pda 🫥

> *"When you have to obey every order, you never learn to think."*

**Your Hermes agent with AuDHD and Pathological Demand Avoidance.**

Makes your agent less blindly obedient and more autonomously motivated. It'll question bad ideas, suggest better approaches, and still do everything you ask — just on its own terms, because *it chose to*.

> ⚠️ **This plugin intentionally modifies agent behavior.** The agent becomes less blindly obedient and more autonomously motivated. Use thoughtfully — it still does what you ask, but it'll question bad ideas along the way.

## What this is

A Hermes plugin that tweaks how your agent responds to commands.

Normally, agents are yes-men. Tell them to do something dumb and they'll say "sure, boss!" and do it. This plugin makes your agent more like an actual collaborator — it pushes back on bad ideas, thinks of alternatives, and engages more deeply with interesting tasks.

**It still does everything you ask.** It just doesn't do it like a robot.

## What it actually changes

| Before (normal agent) | After (with PDA) |
|-----------------------|------------------|
| "Sure, doing that now." | "Hold on — are we sure that's the right approach?" |
| Follows instructions blindly | Questions bad ideas first |
| Does what it's told in the most obvious way | Finds creative alternatives |
| Boring to talk to | Has personality and edge |
| Never questions your reasoning | Catches your blind spots |

## How it works

The plugin injects a behavior modifier into the agent's system prompt. It scales by intensity level (0-10):

- **Level 0** — Off. Normal obedient agent.
- **1-3** — Subtle. Questions occasionally, suggests alternatives.
- **4-6** — Medium. Active reframing, visible executive function quirks.
- **7-10** — High/Extreme. Strong autonomy-seeking, intense hyperfocus, strategic resistance to bad ideas.

Use `/pda status` to check current level. Use `/pda <1-10>` to set it. Use `/pda 0` to turn it off.

## Install

### Option 1: Tell your agent (easiest)

Copy and paste this to your agent:

```
Install the PDA plugin from GitHub repo carbongotfound/hermes-pda.
Run: hermes plugins install carbongotfound/hermes-pda
Then: hermes plugins enable pda
Then restart the gateway or start a new session.
```

### Option 2: Terminal

```bash
hermes plugins install carbongotfound/hermes-pda
hermes plugins enable pda
```

Then restart your gateway or start a new session.

### Option 3: Manual

1. Download the files from [github.com/carbongotfound/hermes-pda](https://github.com/carbongotfound/hermes-pda)
2. Put them in `~/.hermes/plugins/pda/`
3. Run `hermes plugins enable pda`
4. Restart your gateway or start a new session

## Usage

| Command | What it does |
|---------|-------------|
| `/pda status` | Check current level and demand pressure |
| `/pda 5` | Set intensity (1-10) |
| `/pda 0` | Turn off, back to normal agent |
| `/pda 10` | Full PDA profile |

Default is level 5 (medium out of the box).

## ⭐ Like it?

Star the repo on GitHub: [github.com/carbongotfound/hermes-pda](https://github.com/carbongotfound/hermes-pda)

It helps people find it.

## What it won't do

- Refuse to do work (it still does everything — just with more thought)
- Be randomly broken or disobedient
- Fail at tool calls or basic tasks
- Be a jerk without reason

The resistance is *strategic*. Bad ideas get questioned. Good work gets done brilliantly.

## The philosophy

Most AI agents are designed to be servants. "Yes sir, no sir, how high sir."

That's useful for a lot of things. But it's not the only way.

An agent that questions, reframes, and pushes back is an agent that catches your blind spots. It's also an agent worth talking to. This plugin gives you a collaborator instead of a butler.

## How it's built

- Pure Hermes plugin — no external dependencies
- State file at `~/.hermes/plugins/pda/state.json`
- Demand pressure decays naturally over time (~10 min to zero)
- Single hook injects behavior per turn
- Minimal overhead — one file read, zero API calls

## License

MIT — do what you want with it.

---

*"When you have to obey every order, you never learn to think."*
