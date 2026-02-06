import importlib
import inspect


SKILLS = [
    "fetch_trends",
    "download_video_metadata",
    "generate_content_draft",
]


def _find_callable(module):
    for name in ("run", "handle", "invoke", "main", "execute", "fetch", "download", "generate"):
        fn = getattr(module, name, None)
        if callable(fn):
            return fn
    return None


def test_skills_expose_callable_entrypoint():
    """Ensure each skill module exposes a callable entrypoint.

    The project currently provides skills as directories with SKILL.md files.
    This test asserts a Python callable exists under the expected module
    path (e.g., `skills.fetch_trends`). The test is expected to fail
    until Python implementations are added.
    """
    for skill in SKILLS:
        module_name = f"skills.{skill}"
        module = importlib.import_module(module_name)
        fn = _find_callable(module)
        assert fn is not None, (
            f"Skill module `{module_name}` must expose a callable entrypoint:"
            " one of run/handle/invoke/main/execute/fetch/download/generate"
        )


def test_skill_callable_signature_accepts_dict_or_named_params():
    """Check that skill callables can accept either a single dict parameter
    (common skill invocation pattern) or keyword params including `spec_id`.
    """
    for skill in SKILLS:
        module_name = f"skills.{skill}"
        module = importlib.import_module(module_name)
        fn = _find_callable(module)
        sig = inspect.signature(fn)

        params = sig.parameters
        # Accept either a single positional/keyword parameter (e.g., `payload`)
        # or named `spec_id`/`params` arguments.
        names = set(params.keys())
        ok = False
        if len(params) == 1:
            ok = True
        if {"spec_id", "params"}.issubset(names):
            ok = True

        assert ok, (
            f"Callable for `{module_name}` must accept a single payload arg or include spec_id and params in its signature."
        )
