# Login Functionality - Test Execution Report

**Website:** https://www.saucedemo.com/
**Test Type:** Selenium Automation (Python)
**Total Test Cases:** 10
**Total Passed:** 10
**Total Failed:** 0

---

## Test Results Summary

| Test Case ID | Description | Type | Result |
|---|---|---|---|
| TC_01 | Valid login - standard_user | Positive | PASSED |
| TC_02 | Locked out user | Negative | PASSED |
| TC_03 | Wrong password | Negative | PASSED |
| TC_04 | Wrong username | Negative | PASSED |
| TC_05 | Empty username field | Negative | PASSED |
| TC_06 | Empty password field | Negative | PASSED |
| TC_07 | Both fields empty | Negative | PASSED |
| TC_08 | Valid login - problem_user | Positive | PASSED |
| TC_09 | Valid login - performance_glitch_user | Positive | PASSED |
| TC_10 | Both credentials wrong | Negative | PASSED |

---

## Detailed Test Case Results

---

### TC_01 - Login with valid credentials (standard_user)

**Type:** Positive

**Steps:**
1. Open https://www.saucedemo.com/
2. Enter username: standard_user
3. Enter password: secret_sauce
4. Click Login button

**Expected Result:** User is redirected to the inventory page

**Actual Result:** User successfully logged in and redirected to inventory page

**Status:** PASSED

---

### TC_02 - Login with locked out user

**Type:** Negative

**Steps:**
1. Open https://www.saucedemo.com/
2. Enter username: locked_out_user
3. Enter password: secret_sauce
4. Click Login button

**Expected Result:** Error message displayed, user not allowed to login

**Actual Result:** Epic sadface: Sorry, this user has been locked out.

**Status:** PASSED

---

### TC_03 - Login with wrong password

**Type:** Negative

**Steps:**
1. Open https://www.saucedemo.com/
2. Enter username: standard_user
3. Enter password: wrongpassword123
4. Click Login button

**Expected Result:** Error message displayed, login rejected

**Actual Result:** Epic sadface: Username and password do not match any user in this service

**Status:** PASSED

---

### TC_04 - Login with wrong username

**Type:** Negative

**Steps:**
1. Open https://www.saucedemo.com/
2. Enter username: random_user
3. Enter password: secret_sauce
4. Click Login button

**Expected Result:** Error message displayed, login rejected

**Actual Result:** Epic sadface: Username and password do not match any user in this service

**Status:** PASSED

---

### TC_05 - Login with empty username field

**Type:** Negative

**Steps:**
1. Open https://www.saucedemo.com/
2. Leave username field empty
3. Enter password: secret_sauce
4. Click Login button

**Expected Result:** Error message asking for username

**Actual Result:** Epic sadface: Username is required

**Status:** PASSED

---

### TC_06 - Login with empty password field

**Type:** Negative

**Steps:**
1. Open https://www.saucedemo.com/
2. Enter username: standard_user
3. Leave password field empty
4. Click Login button

**Expected Result:** Error message asking for password

**Actual Result:** Epic sadface: Password is required

**Status:** PASSED

---

### TC_07 - Login with both fields empty

**Type:** Negative

**Steps:**
1. Open https://www.saucedemo.com/
2. Leave both username and password fields empty
3. Click Login button

**Expected Result:** Error message displayed

**Actual Result:** Epic sadface: Username is required

**Status:** PASSED

---

### TC_08 - Login with problem_user

**Type:** Positive

**Steps:**
1. Open https://www.saucedemo.com/
2. Enter username: problem_user
3. Enter password: secret_sauce
4. Click Login button

**Expected Result:** User is redirected to the inventory page

**Actual Result:** problem_user logged in and redirected to inventory page successfully

**Status:** PASSED

---

### TC_09 - Login with performance_glitch_user

**Type:** Positive

**Steps:**
1. Open https://www.saucedemo.com/
2. Enter username: performance_glitch_user
3. Enter password: secret_sauce
4. Click Login button

**Expected Result:** User is redirected to inventory page (may take longer than usual)

**Actual Result:** performance_glitch_user logged in successfully, page loaded slow but worked

**Status:** PASSED

---

### TC_10 - Login with completely fake credentials

**Type:** Negative

**Steps:**
1. Open https://www.saucedemo.com/
2. Enter username: fakeuser
3. Enter password: fakepass
4. Click Login button

**Expected Result:** Error message displayed, login rejected

**Actual Result:** Epic sadface: Username and password do not match any user in this service

**Status:** PASSED

---

## Observations

- All 10 test cases passed successfully with no failures.
- The website correctly blocks locked out users with a clear error message.
- Empty field validations are working — username is checked first before password.
- Wrong credentials always show the same generic error message which is good practice as it does not reveal which field is wrong.
- performance_glitch_user takes noticeably longer to load compared to other users but login still works.
- problem_user logs in fine but may show visual issues on the inventory page after login.

---

*End of Report*
