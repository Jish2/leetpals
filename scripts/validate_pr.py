import sys
import requests
from utils.yaml_utils import parse_yaml, parse_yaml_file
from utils.rest_utils import website_is_up
from utils.write_action_output import set_multiline_output
from utils.leetcode_utils import user_is_cracked_at_leetcode

n = len(sys.argv)

github_username = sys.argv[1]
changed_files = sys.argv[2:]
ORIGINAL_SITES_PATH = (
    "https://raw.githubusercontent.com/Jish2/leetpals/refs/heads/main/sites.yaml"
)
OUTPUT_VAR = "VALIDATION_OUTPUT"


def validate_pr(github_username):
    response = requests.get(ORIGINAL_SITES_PATH)
    original_sites = parse_yaml(response.text)
    try:
        new_sites = parse_yaml_file("sites.yaml")
    except Exception:
        new_sites = parse_yaml_file("../sites.yaml")
    # assert one site per gh user
    user_count = 0

    for site in new_sites:
        if site["username"] == github_username:
            user_count += 1

    if user_count != 1:
        text = "Do you type your github username wrong?"
        if user_count > 1:
            text = "One site per user please."
        set_multiline_output(
            OUTPUT_VAR,
            text,
        )
        sys.exit(-1)

    diff = []

    for site in new_sites:
        if not original_sites or site not in original_sites:
            diff.append(site)

    if len(diff) > 1:
        set_multiline_output(
            OUTPUT_VAR,
            "You have changed more than one site in your PR. Please only add one site per PR.",
        )
        sys.exit(-1)

    if len(diff) == 0:
        set_multiline_output(
            OUTPUT_VAR,
            "Did you even change anything...",
        )
        sys.exit(-1)

    change = diff[0]

    # check only valid fields are added
    assert "username" in change
    assert "url" in change
    assert "lc_username" in change
    assert len(change) == 3

    if change["username"] != github_username:
        set_multiline_output(
            OUTPUT_VAR,
            "Don't touch other peoples sites please.",
        )
        sys.exit(-1)

    if not website_is_up(change["url"]):
        set_multiline_output(OUTPUT_VAR, "The site you have added is not live.")
        sys.exit(-1)

    if not user_is_cracked_at_leetcode(change["lc_username"]):
        set_multiline_output(OUTPUT_VAR, "Get Good at Leetcode.")
        sys.exit(-1)


# assert that user has only edited sites.yaml

if len(changed_files) > 1 and "sites.yaml" in changed_files:
    set_multiline_output(
        OUTPUT_VAR,
        "Please do not include sites.yaml changes in a PR with code changes.",
    )
    sys.exit(-1)

if len(changed_files) == 1 and changed_files[0] == "sites.yaml":
    try:
        validate_pr(github_username)
    except Exception as e:
        set_multiline_output(OUTPUT_VAR, "Skill Diff")
        sys.exit(-1)

set_multiline_output(
    OUTPUT_VAR,
    "LGTM!",
)
