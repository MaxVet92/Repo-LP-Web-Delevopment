# Code Review Notes

## Punctuation / Style / General

1. **Variable naming: lowercase**
   - Variables should be written in lowercase (e.g., `bmi` instead of `BMI`).
   - Do not start variable names with a capital letter (e.g., `category` not `Category`) — reserve CapitalizedNames for classes.

2. **Variable names should be descriptive**
   - Names should clearly describe what the variable/function does.
   - Example: `get_bmi_category` instead of `BMI_cat`.

3. **Use f-strings instead of `+` for concatenation**
   - Example:
     ```python
     print(f"{name}, your BMI is: {bmi}. Your weight category therefore is: {category}")
     ```

4. **Keep code inside functions or classes**
   - Every part of the code should be part of a function or class (i.e., part of an “object”).
   - The only code allowed outside is:
     ```python
     if __name__ == "__main__":
         pass
     ```
   - Video explanation: https://www.youtube.com/watch?v=x5IbdKnvt6k

5. **Comments formatting**
   - Do not use `###` or `##` for comments.
   - Use only `#` and a space after it, e.g.:
     ```python
     # this is my comment
     ```

6. **Blank lines**
   - Only **one** blank line between loops / `if` blocks.
   - **Two** blank lines are only to be used between classes / functions.

7. **No space before `:`**
   - Write `if x:` not `if x :`

8. **File naming**
   - Python file names should always be lowercase.

---

## Functional Feedback

The code is working — great.

1. **Input prompt formatting**
   - Add a space after `Enter your name:` so it looks nicer (e.g., `"Enter your name: "`).

2. **Realistic weight validation**
   - Add a rule that weight must be realistic (e.g., user should not be able to enter `5 kg`).

3. **Exception formatting**
   - Use:
     ```python
     except ValueError:
     ```
     instead of `except:ValueError`