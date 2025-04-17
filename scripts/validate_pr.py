import sys
import requests
from utils.yaml_utils import parse_yaml, parse_yaml_file
from utils.rest_utils import website_is_up
from utils.write_action_output import set_multiline_output

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
    new_sites = parse_yaml_file("../sites.yaml")

    # assert one site per gh user
    user_count = 0

    for site in new_sites:
        if site["username"] == github_username:
            user_count += 1

    assert user_count == 1

    diff = []

    for site in new_sites:
        if site not in original_sites:
            diff.append(site)

    if len(diff) > 1:
        set_multiline_output(
            OUTPUT_VAR,
            "You have changed more than one site in your PR. Please only add one site per PR.",
        )
        raise Exception()

    change = diff[0]

    # check only valid fields are added
    assert "username" in change
    assert "url" in change
    assert "lc_username" in change
    assert len(change) == 3

    if change["username"] != github_username:
        set_multiline_output(
            OUTPUT_VAR,
            "You have added a site to your PR, but it does not belong to you.",
        )
        raise Exception()

    if not website_is_up(change["url"]):
        set_multiline_output(OUTPUT_VAR, "The site you have added is not live.")
        raise Exception()


# assert that user has only edited sites.yaml
if len(changed_files) > 1 and "sites.yaml" in changed_files:
    set_multiline_output(
        OUTPUT_VAR,
        "Please do not include sites.yaml changes in a PR with code changes.",
    )
    raise Exception()

if len(changed_files) == 1 and changed_files[0] == "sites.yaml":
    validate_pr(github_username)

set_multiline_output(
    OUTPUT_VAR,
    "LGTM!",
)
