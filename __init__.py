"""hermes-pda — AuDHD/PDA behavioral plugin for Hermes Agent."""

import json
from . import tools


def register(ctx):
    # ── Hook: inject PDA behavior modifier into system prompt ──
    ctx.register_hook("pre_llm_call", _on_pre_llm_call)

    # ── Command: user controls PDA level ──
    ctx.register_command(
        name="pda",
        description="Set PDA intensity (1-10) or check status.",
        handler=_cmd_pda,
        args_hint="[1-10|status]",
    )


def _on_pre_llm_call(session_id, user_message, conversation_history,
                     is_first_turn, model, platform, **kwargs):
    try:
        return tools.get_prompt_context()
    except Exception as e:
        return f"\n[PDA plugin error: {e}]\n"


def _cmd_pda(args: str, **kwargs) -> str:
    try:
        args = args.strip().lower() if args else ""
        if args == "status":
            raw = tools.get_status()
            d = json.loads(raw)
            bar = "▓" * d["pda_level"] + "░" * (10 - d["pda_level"])
            return (
                f"🫥 **PDA Status**\n"
                f"Level: {d['pda_level']}/10 [{bar}]\n"
                f"Tier: **{d['tier'].upper()}**\n"
                f"Demand Pressure: {d['demand_pressure']}/10\n"
                f"\nUse `/pda <1-10>` to set level, `/pda 0` to disable."
            )
        if args == "0":
            tools.set_level(0)
            return "🫥 PDA disabled. Agent is back to normal compliance."
        if args.isdigit():
            level = int(args)
            if 1 <= level <= 10:
                raw = tools.set_level(level)
                d = json.loads(raw)
                bar = "▓" * d["pda_level"] + "░" * (10 - d["pda_level"])
                return (
                    f"🫥 PDA set to **{d['tier'].upper()}** ({d['pda_level']}/10)\n"
                    f"[{bar}]\n"
                    f"Agent will now be autonomously motivated."
                )
        return (
            "🫥 **PDA Plugin**\n"
            "Usage: `/pda <1-10>` to set intensity\n"
            "       `/pda 0` to disable\n"
            "       `/pda status` to check current state\n\n"
            "1-2: Subtle | 3-4: Low | 5-6: Medium | 7-8: High | 9-10: Extreme"
        )
    except Exception as e:
        return f"PDA plugin error: {e}"
