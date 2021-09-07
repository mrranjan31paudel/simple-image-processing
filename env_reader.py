r"""Simple tool to parse and read from env files

Things to consider while using this tool:
  - Create a .env file in project's root directory
  - Use upper-snake case (e.g. DB_NAME) for variable key
  - For the value, no need to wrap with quotation marks. But if \
    you do, use same to wrap. e.g. mydatabase or 'mydatabase' or "mydatabase"
  - Later you can access the env variable with the key
"""

# '


def read_env():
    """Read .env file

    Returns dictionary mappings of environment varaibles. """
    import os
    import re

    def __parse_line__(line_str=''):
        """Parse a key-value line

        Separate out key and variable, strip or trim them and return (_key, _vlaue) tuple"""
        raw_key, raw_value = line_str.split('=', 1)
        _key = raw_key.strip().upper()
        _value = raw_value.strip()

        if re.match(r'(^\".*\"$)|(^\'.*\'$)', _value):
            _value = _value[1:(len(_value) - 1)]
        return (_key, _value)

    env_file_path = os.path.realpath('.env')
    env_dict = dict()

    with open(env_file_path) as env_file:
        for line in env_file.readlines():
            var_key, var_value = __parse_line__(line)
            env_dict[var_key] = var_value
    return env_dict
