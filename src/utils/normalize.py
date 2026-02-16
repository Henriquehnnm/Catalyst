from readers.parser import main_reader

KEYWORD_MAP = {
    # ===== PASSED =====
    "passed": "passed",
    "pass": "passed",
    "ok": "passed",
    "success": "passed",
    "successful": "passed",
    "succeed": "passed",
    "green": "passed",
    "ok_": "passed",
    
    # ===== FAILED =====
    "failed": "failed",
    "fail": "failed",
    "error": "failed",
    "failure": "failed",
    "err": "failed",
    "broken": "failed",
    "red": "failed",
    "timeout": "failed",
    "timedout": "failed",
    "exception": "failed",
    "crash": "failed",
    "crashed": "failed",
    "aborted": "failed",
    "abort": "failed",
    
    # ===== SKIPPED =====
    "skipped": "skipped",
    "skip": "skipped",
    "ignored": "skipped",
    "ignore": "skipped",
    "disabled": "skipped",
    "disable": "skipped",
    "pending": "skipped",
    "todo": "skipped",
    "not_run": "skipped",
    "notrun": "skipped",
    "yellow": "skipped",
    "omitted": "skipped",
    "omit": "skipped",
}

def main_normalise(value: str) -> str:
    clean = value.strip().lower()
    return KEYWORD_MAP.get(clean, "unknown")

data = main_reader()
print(main_normalise(data))
