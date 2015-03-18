import json

config = {}
config["treebank"] = json.load(open("./app/configurations/treebank.json", "r"))
config["session"] = json.load(open("./app/configurations/session.json", "r"))
config["cts"] = json.load(open("./app/configurations/cts.json", "r"))


def get(key):
    """
    @param  key  string  Key representing the subset of configurations concerned
    @type
    @returns function
    """
    return lambda s: config[key][s]