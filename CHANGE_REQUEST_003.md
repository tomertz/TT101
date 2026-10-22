# Change Request 003: Web Version of the Converter

| Field | Value |
|-------|-------|
| **Change request** | CR-003 |
| **Date** | October 22, 2026 |
| **Requested by** | tomertz |
| **Applies to** | [REQUIREMENTS.md](REQUIREMENTS.md) |
| **Status** | Approved, implementation waiting for browser test |
| **Approved** | October 22, 2026, by tomertz |

## Summary

Add a web page version of the unit converter that anyone can use in a browser, without installing Python. The page runs the existing `converter.py` code in the browser using [PyScript](https://pyscript.net), and is hosted for free on GitHub Pages from the `tomertz/TT101` repository.

The console app (`py converter.py`) keeps working exactly as it does today.

## Reason for the change

The console app only works on a computer with Python installed, and it has to be started from a terminal. A web page works on any computer or phone with a browser.

## Approach

- **PyScript** loads a Python interpreter into the browser, so the web page uses the same `convert()` function as the console app. The conversion logic is written and tested once, and both versions always give the same results.
- **GitHub Pages** publishes the page from the repository for free. The page updates automatically after each push to `main`.
- The page lives in a `converter` folder in the repository, so it will be available at **https://tomertz.github.io/TT101/converter/**. It loads `converter.py` from the repository's main folder, so there is only one copy of the conversion code.
- The repository's main address, https://tomertz.github.io/TT101/, shows the README, which GitHub Pages displays automatically when there's no web page in the main folder. The README will link to the converter page.

**Trade-off:** the first time someone opens the page, the browser downloads Python, which takes a few seconds. Later visits are faster because the browser keeps a copy.

## Page behavior

These are proposed defaults. Each one can be changed before this change request is approved.

### Layout

From top to bottom, the page shows:

1. The title **Unit Converter**.
2. A number box and a unit dropdown side by side.
3. The result, in large text, for example `160.93 km`.
4. The list of available conversions, matching the console startup screen.

### Input: a number box and a unit dropdown

The user types a number and picks a unit from a dropdown, instead of typing `100 mi` into one box. A dropdown makes unknown units impossible and works better on phones. Each dropdown option shows the unit code, its name, and what it converts to, for example `mi (miles) → km`. The default selection is `mi`.

### Result updates as you type

There is no Convert button. The result updates as soon as the number or the unit changes. When the number box is empty, no result is shown.

### Invalid values

The same rules as the console app apply: negative numbers are invalid except for temperatures, and temperatures can't be below absolute zero. Because the dropdown prevents unknown units, the console error message doesn't fit, so the page shows this instead, in place of the result:

```
Invalid value. Only temperatures (c, f) can be negative, and not below absolute zero.
```

### While loading

Until Python finishes loading, the input controls are disabled and the result area shows `Loading converter...`.

### Not included

- The "Press any key to continue..." step, because the result stays on the page.
- A quit option, because the user just closes the page.

## Changes to REQUIREMENTS.md

Add a new "Web version" section after "Platform" that contains the "Approach" and "Page behavior" sections of this change request. The existing requirements for the console app don't change.

## What doesn't change

- `converter.py` keeps working as a console app with the same behavior.
- The supported units, conversion formulas, rounding, and validation rules. The web page uses the same `convert()` function.
- The existing tests.

## Affected files

| File | Change |
|------|--------|
| `converter/index.html` | New. The web page's layout and styling. Uses PyScript release 2026.7.3, which runs Pyodide 314.0.3. |
| `converter/main.py` | New. The PyScript code that connects the page to `convert()`. |
| `converter/pyscript.json` | New. PyScript settings that copy `converter.py` into the browser. |
| `converter.py` | No change expected. If a small change is needed so the page can load it, it must not change the console app's behavior. |
| `REQUIREMENTS.md` | Add the "Web version" section. |
| `README.md` | Add a link to the web page and how to try the page on your own computer. |

## Publishing steps

1. Merge `converter/index.html` into the `main` branch and push it.
2. In the repository on GitHub, open **Settings → Pages**, set **Source** to **Deploy from a branch**, choose `main` and the `/ (root)` folder, and select **Save**. This is a one-time step that the repository owner does on the GitHub website.
3. Wait a minute or two, then open https://tomertz.github.io/TT101/converter/.

GitHub Pages is free for public repositories, which `tomertz/TT101` is.

## Testing

- The existing unit tests must still pass.
- The page will be tested in a browser on this computer before publishing, by running a local web server with `py -m http.server` and opening `http://localhost:8000/converter/`.
- After publishing, the live page will be checked at the GitHub Pages address.

### Known issue: corporate network filter

On the requester's company network, the Zscaler security filter blocks `python_stdlib.zip`, a file Pyodide needs to start, so the page stays on `Loading converter...`. Other Pyodide files download normally. Because of this:

- The full browser test must be done from a computer or network without Zscaler, such as a home network or a phone on mobile data.
- Users on the same company network will see the same problem unless the filter allows `https://cdn.jsdelivr.net/pyodide/`.
- If this becomes a problem, PyScript can use MicroPython instead of Pyodide. Its files do get through the filter, but switching needs its own change request and testing.

The page logic in `converter/main.py` has been tested on this computer by running it in regular Python with a stand-in for the browser.

## Acceptance criteria

- The page loads and shows `Loading converter...` until it's ready.
- Every unit is in the dropdown, and every example from `REQUIREMENTS.md` gives the same result on the page as in the console app.
- Negative values and temperatures below absolute zero show the invalid-value message.
- Clearing the number box clears the result.
- The page is usable on a phone-sized screen.
- `py converter.py` still works as before, and all existing tests pass.
