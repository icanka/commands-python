from .entry import cadet
from importlib.metadata import entry_points
from pprint import pprint

print("INIT.PY")

# Advertise a new group of entry points.
# We expect a plugin package to implement this entry point
# to supply us a subcommand.
entry_point_group = entry_points(group='cadet.cli')

try:
    pprint(entry_point_group)
    implementers = entry_point_group[0].load()
    cadet.add_command(implementers)

except IndexError:
    print("No implementors")

