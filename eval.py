import json
import sys
from pprint import pprint

# --- mock endpoint ---
def call_model(prompt):
    if "leave" in prompt.lower():
        return "14 days annual leave"
    if "travel" in prompt.lower():
        return "Direct manager"
    return "Unknown"

# --- simple scoring (exact match) ---
def score(pred, expected):
    return pred.strip().lower() == expected.strip().lower()

# --- main ---
def run(file_path):
    total, passed = 0, 0
    failures = []

    with open(file_path) as f:
        for line in f:
            try:
                row = json.loads(line)
                input = row["input"]
                expected = row["expected"]
                pred = call_model(input)
                ok = score(pred, expected)

                total += 1
                if ok:
                    passed += 1
                else:
                    failures.append({
                        "id": row["id"],
                        "input": input,
                        "expected": expected,
                        "prediction": pred
                    })

            except Exception as e:
                failures.append({"error": str(e)})

    print(f"Pass rate: {passed}/{total} = {passed/total:.2f}")
    print("Failures:")
    pprint(failures)

if __name__ == "__main__":
    run(sys.argv[1])