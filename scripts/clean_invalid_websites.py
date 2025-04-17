from utils.rest_utils import website_is_up
from utils.yaml_utils import parse_yaml_file, write_yaml
from utils.write_action_output import set_multiline_output

sites = parse_yaml_file("sites.yaml")

invalid_sites = []
valid_sites = []

for item in sites:
    username = item["username"]
    url = item["url"]

    if not website_is_up(url):
        invalid_sites.append(item)
    else:
        valid_sites.append(item)

write_yaml("sites.yaml", valid_sites)

action_output = "### Removed Sites and Owners\n\n"
for site in invalid_sites:
    action_output += f"@{site['username']}: {site['url']}\n"

set_multiline_output("SCRAPER_OUTPUTS", action_output)
