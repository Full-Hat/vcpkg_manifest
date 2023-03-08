import re
import sys
import json

###!!! Settings
boost_version = "1.79.0"
input_file_name = "cmake_output_for_gen"
###!!!

###!!!
# Usage:
# 

def get_boost_libraries(input_string):
    pattern = r"boost-[a-zA-Z0-9]+"
    matches = re.findall(pattern, input_string)
    return list(set(matches))

def generate_overrides(boost_libraries, param_value):
    overrides = []
    for library in boost_libraries:
        overrides.append({
            "name": library,
            "version": param_value
        })
    return json.dumps({"overrides": overrides}, indent=4)

if not __name__ == "__main__":
    # check input 
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <boost_version>")
        sys.exit(1)
    input_file_name = sys.argv[1]
    boost_version = sys.argv[2]

# parse boost libraries names
input_file = input_file_name
with open(input_file, 'r') as f:
    input_string = f.read()

boost_libraries = get_boost_libraries(input_string)

# generate overrides
boost_libraries = json.loads(str(boost_libraries).replace("'", "\""))
param_value = boost_version

overrides_string = json.loads(generate_overrides(boost_libraries, param_value))

# replace previous overrides with new
with open("vcpkg.json", 'r') as f:
    manifest_data = f.read()

data = json.loads(manifest_data)
data["overrides"] = [override for override in data["overrides"] if "boost" not in override["name"]]
new_overrides = overrides_string["overrides"]
for override_el in new_overrides:
    if override_el["name"] == "boost-config":
        continue
    data["overrides"].append(override_el)
#data["overrides"] = overrides_string["overrides"]

result_manifest = json.dumps(data, indent=4)

# save result manifest
with open("new_vcpkg.json", 'w') as f:
    f.write(result_manifest)

print("result saved to \"new_vcpkg.json\"")
