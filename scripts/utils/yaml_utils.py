import yaml


def parse_yaml(filepath):
    with open(filepath) as stream:
        try:
            parsed_yaml = list(yaml.safe_load(stream))
            return parsed_yaml
        except yaml.YAMLError as exc:
            print(exc)
    return None


def write_yaml(filepath, data):
    with open(filepath, "w") as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
