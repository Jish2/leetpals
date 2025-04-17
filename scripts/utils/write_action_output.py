import os
import uuid


def set_multiline_output(name, value):
    try:
        with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
            delimiter = uuid.uuid1()
            print(f"{name}<<{delimiter}", file=fh)
            print(value, file=fh)
            print(delimiter, file=fh)
    except Exception:
        # testing locally, just print to console
        print(value)
