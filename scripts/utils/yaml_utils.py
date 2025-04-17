import yaml


def parse_yaml(string):
    return yaml.safe_load(string)


def parse_yaml_file(filepath):
    with open(filepath) as stream:
        try:
            return parse_yaml(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return None


def write_yaml(filepath, data):
    with open(filepath, "w") as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
