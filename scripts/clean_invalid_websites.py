from utils.rest_utils import website_is_up
from utils.yaml_utils import parse_yaml, write_yaml
from utils.write_action_output import set_multiline_output

sites = parse_yaml("..//sites.yaml")

invalid_sites = []
valid_sites = []

for item in sites:
    username = item["username"]
    url = item["url"]

    if not website_is_up(url):
        invalid_sites.append(item)
    else:
        valid_sites.append(item)

write_yaml("..//sites.yaml", valid_sites)

action_output = ""
for site in invalid_sites:
    action_output += f"@{site['username']} - {site['url']}\n"

set_multiline_output("OUTPUT", action_output)
