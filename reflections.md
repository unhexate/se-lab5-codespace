# Static Analysis Lab Reflection

1. Easiest and Hardest Issues to Fix  
- The easiest issues were missing docstrings, spacing, and naming convention violations These changes were straightforward because they mainly involved improving readability and following style rules.  
- The hardest issues were those related to design and security, such as removing the use of eval, replacing it with ast.literal_eval, and avoiding global variables. These required refactoring the logic to ensure functionality remained correct while improving safety.

2. False Positives  
- One possible false positive was the warning about using a mutable default argument. In this specific case, the default list was not reused across calls, so it would not have caused an issue. However, I still corrected it to follow best practices and prevent potential bugs in the future.

3. Integration into Workflow  
Static analysis tools can be added into both local development and CI workflows. Developers can run tools like Pylint, Bandit, and Flake8 before committing code to catch errors early. In continuous integration systems such as GitHub Actions or GitLab CI, these tools can be set up to automatically check each commit or pull request and block merges if issues are detected.

4. Tangible Improvements  
After applying fixes, the code became cleaner, more readable, and easier to maintain. It now follows Python’s PEP 8 conventions, uses safer file handling with context managers, and avoids risky functions like eval. The result is more secure, predictable, and maintainable code.
