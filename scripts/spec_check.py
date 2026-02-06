#!/usr/bin/env python3
"""Simple spec-check script.

Verifies that `skills/*` Python modules expose a callable entrypoint and
that the callable accepts either a single payload argument or named
`spec_id` and `params` arguments. Exits with non-zero code on failures.
"""
import importlib
import inspect
import os
import sys


SKILLS_DIR = os.path.join(os.path.dirname(__file__), "..", "skills")
SKILLS = [d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))]


def find_callable(module):
    for name in ("run", "handle", "invoke", "main", "execute", "fetch", "download", "generate", "fetch_trends"):
        fn = getattr(module, name, None)
        if callable(fn):
            return fn
    return None


def check_skill(skill):
    module_name = f"skills.{skill}"
    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        return False, f"ImportError for {module_name}: {e}"

    fn = find_callable(module)
    if not fn:
        return False, f"No callable entrypoint found in {module_name}"

    sig = inspect.signature(fn)
    names = set(sig.parameters.keys())
    if len(sig.parameters) == 0:
        return False, f"Callable in {module_name} must accept at least one parameter"
    if len(sig.parameters) == 1:
        return True, "OK"
    if {"spec_id", "params"}.issubset(names):
        return True, "OK"

    return False, f"Callable in {module_name} has unexpected signature: {sig}"


def main():
    failures = []
    print(f"Checking skills in {SKILLS_DIR}: {SKILLS}")
    for s in SKILLS:
        ok, msg = check_skill(s)
        if ok:
            print(f"[OK] {s}: {msg}")
        else:
            print(f"[ERROR] {s}: {msg}")
            failures.append((s, msg))

    if failures:
        print('\nSpec-check failed: {} failures'.format(len(failures)))
        sys.exit(2)

    print('\nSpec-check passed')
    sys.exit(0)


if __name__ == "__main__":
    main()
