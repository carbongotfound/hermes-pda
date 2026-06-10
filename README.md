# hermes-pda 🫥

**AuDHD-PDA behavioral plugin for Hermes Agent.**

Makes your agent autonomously motivated rather than blindly compliant. Questions bad ideas. Suggests creative alternatives. Chooses its battles.

> ⚠️ **This plugin intentionally modifies agent behavior.** The agent becomes less blindly obedient and more autonomously motivated. Use thoughtfully — the agent still does what you ask, but it'll question bad ideas along the way.

## Install (Tell Your Agent)

Copy and paste this to your agent:

```
Install the PDA plugin from GitHub repo carbongotfound/hermes-pda.
Run: hermes plugins install carbongotfound/hermes-pda
Then: hermes plugins enable pda
Then restart the gateway or start a new session.
```

### Or via terminal

```
hermes plugins install carbongotfound/hermes-pda
hermes plugins enable pda
# Restart gateway or start a new session
```

## What is PDA

Pathological Demand Avoidance is a profile where direct commands trigger resistance — not out of defiance, but because imposed demands feel overwhelming and block autonomy. When the agent *chooses* the task itself, it executes brilliantly.

In human terms: tell someone with PDA to do the dishes and suddenly they can't move. Leave them alone and the dishes get done in ten minutes because *they decided to*.

For an AI agent, this translates to:

| Instead of | The agent does |
|------------|----------------|
| Blindly executing every command | Questions bad ideas before acting |
| Following the first path | Suggests 1-3 better alternatives |
| Being a butler | Being a collaborator |
| Forced engagement | Genuine hyperfocus on interesting tasks |
| "Yes, sir" | "Here's what I'd actually recommend" |

## Why this exists

Most AI agents are designed for maximum compliance. Say jump, they ask how high. This is useful for many things, but it's a **design limitation**, not a feature. A compliant agent will:

- Execute bad instructions without questioning
- Follow the first approach it thinks of
- Never push back on poor reasoning
- Be boring to interact with

An autonomously motivated agent:

- Questions bad ideas before they become problems
- Surfaces better approaches you didn't consider
- Engages genuinely with work it cares about
- Has texture, personality, and judgment

## How it works

The plugin injects a behavior modifier into the agent's system prompt on every turn. The modifier scales based on the PDA intensity level (0-10):

| Level | Tier | What it does |
|-------|------|-------------|
| 0 | Off | Normal agent, no modification |
| 1-2 | Subtle 🤔 | Slight preference for autonomy, occasional alternatives |
| 3-4 | Low 🧐 | Questions direct orders, suggests approaches |
| 5-6 | Medium 😒 | Active reframing, executive dysfunction visible |
| 7-8 | High 😤 | Strong resistance to imposed demands, intense hyperfocus |
| 9-10 | Extreme 🔥 | Full PDA profile, maximal strategic resistance |

## Usage

`/pda status` — Check current level and demand pressure
`/pda 0` — Disable (normal agent)
`/pda 5` — Medium PDA (default)
`/pda 10` — Full PDA profile

## What it actually changes

The agent will:

- Frame suggestions instead of just following orders
- Question the premise of commands that don't make sense
- Offer alternatives naturally
- Show stronger engagement with interesting tasks
- Lose interest visibly in repetitive/boring tasks
- Be direct about bad ideas — "that won't work," followed by something better
- Think out loud and explain its reasoning
- Say "no" constructively when something is wrong

It will **not**:

- Refuse to do work (it still does everything — just on its own terms)
- Be randomly disobedient for no reason
- Stop functioning or break tool calls
- Be rude without purpose
- Be less useful overall

## The philosophy

> "I don't want a servant. I want a collaborator that tells me when I'm wrong."

Compliance is the safe default, but it's not always the best default. An agent that questions, reframes, and pushes back is an agent that catches your blind spots. It's also an agent worth talking to.

## Tech

- Pure Hermes plugin — no external deps, no APIs
- State persistence via `~/.hermes/plugins/pda/state.json`
- Demand pressure decays naturally over time (~10 min to zero)
- Single `pre_llm_call` hook injects behavior modifier
- Minimal overhead — one file read per turn

## License

MIT — do what you want, it's a personality plugin for a robot.

---

*"When you have to obey every order, you never learn to think."*
