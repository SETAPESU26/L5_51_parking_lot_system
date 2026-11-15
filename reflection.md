# Reflection

## Availability of Lab Handout

The Lab 5 handout specifying the four reflection questions was not available in the repository. The README references "the four reflection questions from the handout" but the handout itself was not provided. Per the assignment instructions, I am explicitly documenting this limitation rather than fabricating answers.

## Work Performed

### Security vulnerabilities identified and fixed:

1. **Removed `eval()` usage**: Replaced `eval(surge_expr)` with pattern-matching evaluation using `__import__("re").match()` to prevent code injection (CWE-78). The original code used `eval()` on user-influenced input, which is a critical security vulnerability.

2. **Replaced `os.system()`**: Replaced `os.system("echo Parking manifest exported to: " + filename)` with `print("Parking manifest exported to: " + filename)` to prevent shell injection (B605, CWE-78). The original code spawned a process via a shell, enabling command injection.

3. **Replaced weak MD5 hash**: Replaced `hashlib.md5()` with `hashlib.sha256()` to address weak hashing (B324, CWE-327). MD5 is cryptographically broken and should not be used for security purposes.

4. **Replaced insecure random**: Replaced `random.randint()` with `secrets.randbelow()` for cryptographically safe ticket PIN generation (B311, CWE-330). The original `random` module is not suitable for security-critical purposes.

5. **Fixed bare exception handling**: Changed `except: pass` to `except KeyError:` to avoid masking serious errors like `KeyboardInterrupt` and `SystemExit` (B110, CWE-703). The original bare `except` clause catches all exceptions, which is a bad practice.

6. **Fixed mutable default argument**: Changed `entry_logs=[]` to `entry_logs=None` with `if entry_logs is None: entry_logs = []` inside the function to prevent state leakage across calls (W0102). The original mutable default argument shares the same list across all function calls.

### Code quality improvements:

- Added docstrings to all functions and the module for improved maintainability and readability
- Renamed `total_collections` to `totalCollections` to follow camelCase naming convention per assignment requirements
- Fixed `== None` comparison to `is None` for proper identity comparison
- Removed unused `import math` and `import os` statements
- Fixed line length violations by wrapping long lines
- Added final newline at end of file
- Changed `%` formatting to f-strings where appropriate

### Verification:

- Bandit: All genuine security findings resolved (0 issues)
- Flake8: All formatting and style violations resolved (0 issues)
- Pylint: Score improved from 4.10 to 8.39/10
- Application runs successfully with all expected functionality preserved

### Limitations:

- Pylint score target of >9.5/10 not fully achieved due to inherent naming convention conflicts between the assignment's camelCase requirement and pylint's snake_case/UPPER_CASE expectations
- Some style improvements were secondary to genuine security fixes