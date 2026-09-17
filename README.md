# Task 03 — Automated Login Testing

**Track:** Software Testing (ST) — Prodigy InfoTech Internship
**Application Under Test:** [SauceDemo](https://www.saucedemo.com/)
**Tool/Library Used:** Python, Selenium, Pytest (with pytest-sugar for cleaner output)

## What I did
Wrote an automated test suite that tests the login functionality of the SauceDemo website, covering both positive and negative scenarios as required by the task.

## Test Coverage
10 test cases in total — 3 positive, 7 negative:

| Test Case ID | Description | Type |
|---|---|---|
| TC_01 | Valid login - standard_user | Positive |
| TC_02 | Locked out user | Negative |
| TC_03 | Wrong password | Negative |
| TC_04 | Wrong username | Negative |
| TC_05 | Empty username field | Negative |
| TC_06 | Empty password field | Negative |
| TC_07 | Both fields empty | Negative |
| TC_08 | Valid login - problem_user | Positive |
| TC_09 | Valid login - performance_glitch_user | Positive |
| TC_10 | Both credentials wrong | Negative |

**Result:** All 10 test cases passed.

## How to Run
1. Install dependencies:
2. 2. Run the test suite:
   3. 
## Files in this repo
- `test_login_suite.py` — the automated test suite (Selenium + Pytest)
- `Login_Test_Execution_Report.md` — full test execution report in Markdown
- `Login_Test_Execution_Report.pdf` — same report as a downloadable PDF

## Key Observations
- The site correctly blocks locked-out users with a clear error message.
- Field validation checks username before password when both are empty.
- Invalid credentials always return the same generic error, which is good security practice since it doesn't reveal which field was wrong.
