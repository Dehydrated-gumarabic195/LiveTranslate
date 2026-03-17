import locale
import yaml
from pathlib import Path

_strings: dict = {}
_lang = "en"
_dir = Path(__file__).parent / "i18n"


def _detect_system_lang() -> str:
    """Return 'zh' if system locale is Chinese, else 'en'."""
    try:
        lang_code = locale.getdefaultlocale()[0] or ""
        if lang_code.startswith("zh"):
            return "zh"
    except Exception:
        pass
    return "en"


def set_lang(lang: str):
    global _lang, _strings
    _lang = lang
    f = _dir / f"{lang}.yaml"
    if not f.exists():
        f = _dir / "en.yaml"
    _strings = yaml.safe_load(f.read_text("utf-8")) or {}


def get_lang() -> str:
    return _lang


def t(key: str) -> str:
    return _strings.get(key, key)


# Detect system language on import
set_lang(_detect_system_lang())
