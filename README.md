# Lightweight LLM Evaluation Harness

## What this does
This is a simple CLI tool that evaluates a mock LLM endpoint against a JSONL test file.

It:
- reads test cases from a `.jsonl` file
- sends each input to a mock model endpoint
- compares the model response against the expected answer
- reports pass rate and failed cases
- handles basic errors gracefully

## File structure
- `eval.py` — main evaluation script
- `test.jsonl` — sample test cases



## Input format
The input file should be in JSONL format, with one test case per line.

Example:

```json
{"id": "q1", "input": "What is the leave policy?", "expected": "14 days annual leave"}
{"id": "q2", "input": "Who approves travel claims?", "expected": "Direct manager"}
```

Each line must contain:

- id — unique test case id
- input — prompt/question sent to the model
- expected — expected answer


## How to run

Run from terminal:
```bash
python eval.py test.jsonl
```

## How scoring works

This version uses exact match scoring. A test passes if:
- predicted answer == expected answer
- comparison ignores case differences
- leading/trailing spaces are ignored

Example:
- "Direct manager" vs "direct manager " → pass
- "14 days" vs "14 days annual leave" → fail

This is simple and easy to explain, though stricter than real-world evaluation.

Example output
```bash
Pass rate: 4/10 = 0.40
Failures:
[{'expected': '15 days annual leave',
  'id': 'q3',
  'input': 'What is the leave policy?',
  'prediction': '14 days annual leave'},
 {'expected': 'HR manager',
  'id': 'q4',
  'input': 'Who approves travel claims?',
  'prediction': 'Direct manager'},
 {'expected': 'Formal attire',
  'id': 'q5',
  'input': 'What is the dress code?',
  'prediction': 'Unknown'},
 {'expected': 'Performance based bonus',
  'id': 'q6',
  'input': 'Tell me about bonuses',
  'prediction': 'Unknown'},
 {'expected': '14 days',
  'id': 'q7',
  'input': 'What is the leave policy?',
  'prediction': '14 days annual leave'},
 {'expected': '',
  'id': 'q9',
  'input': 'Random question',
  'prediction': 'Unknown'}]
```


## Mock endpoint behavior

The script uses a simple mock endpoint instead of a real LLM.

Current behavior:
- if input contains "leave" → returns "14 days annual leave"
- if input contains "travel" → returns "Direct manager"
- otherwise → returns "Unknown"

This keeps the evaluation harness easy to run without external dependencies.


## Why this design

I chose a CLI tool because it is the fastest and simplest way to satisfy the requirement.

It is easy to:
- run locally
- test quickly
- extend later

The same evaluation logic could later be wrapped into a small API service if needed.



## What I would add with more time

With more time, I would add:

- semantic scoring instead of only exact match
- token-level F1 or similarity-based evaluation
- support for real model/API endpoints
- better reporting in JSON or CSV
- configurable pass thresholds
- more unit tests
- logging and retry logic for endpoint failures


## Notes
- This implementation is intentionally minimal and interview-friendly.
- It focuses on clarity, correctness, and meeting the stated requirements.