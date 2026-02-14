from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path


LIBRARY_ROOT = Path(__file__).resolve().parent


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Failed to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    # Some stdlib features (e.g. dataclasses) expect the defining module to be in sys.modules.
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def cmd_build_book() -> int:
    mod = _load_module("_build_book", LIBRARY_ROOT / "book" / "_build_book.py")
    mod.build()
    return 0


def cmd_improve(argv: list[str]) -> int:
    mod = _load_module(
        "generate_prompt_improvements", LIBRARY_ROOT / "tools" / "context_engineering" / "generate_prompt_improvements.py"
    )
    # Default to operating on this library folder unless the user overrides --root.
    if argv[:1] == ["--"]:
        argv = argv[1:]
    if "--root" not in argv:
        argv = ["--root", str(LIBRARY_ROOT)] + argv
    return int(mod.main(argv))


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="library.py", description="Prompt Ecosystem library entrypoint.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("build-book", help="Rebuild library/book artifacts + ontology exports.")

    p_improve = sub.add_parser("improve", help="Generate improvement artifacts for canonical prompts.")
    p_improve.add_argument("args", nargs=argparse.REMAINDER, help="Args forwarded to the improvement generator.")

    ns = parser.parse_args(argv)

    if ns.cmd == "build-book":
        return cmd_build_book()
    if ns.cmd == "improve":
        return cmd_improve(list(ns.args))
    raise RuntimeError(f"Unknown command: {ns.cmd}")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
