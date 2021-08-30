#include "json.hpp"

#include <algorithm>
#include <iostream>
#include <string>

const std::string filtered_suffix = "filtered";
const char json_delim = '.';

bool str_endswith(std::string &full, const std::string &suffix) {
    return !full.compare(full.length() - suffix.length(), suffix.length(), suffix);
}

int main(int argc, char* argv[])
{
    using json = nlohmann::json;
    bool include_raw = false;

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "-r") {
            include_raw = true;
        }
    }

    for (std::string line; std::getline(std::cin, line);) {
        json j_in = json::parse(line);
        if (!j_in.contains("timestamp") && !j_in.contains("layers")) {
            continue;
        }
        // If no data or layers keys, skip.
        try {
            if (!include_raw) {
                j_in["layers"].erase("data");
            }
        } catch (json::out_of_range) {
            continue;
        } catch (json::type_error) {
            continue;
        }
        j_in = j_in.flatten();
        json j_out;
        // selectively copy/parse flattened fields.
        // TODO: tshark exports some fields as floats, that are really ints - convert them.
        // TODO: convert IP addresses/MAC addresses to ints.
        for (auto& el : j_in.items()) {
            std::string key = el.key();
            // skip filtered field
            if (str_endswith(key, filtered_suffix)) {
                continue;
            }
            // remove initial '/'
            key.erase(0, 1);
            std::replace(key.begin(), key.end(), '/', json_delim);
            std::string val;
            // default passthrough.
            j_out[key] = el.value();
            // get key as a string, or pass through if already not a string.
            try {
                val = el.value().get<std::string>();
            } catch (json::type_error) {
                continue;
            }
            // try to parse as an int or hex string.
            const char *val_str = val.c_str();
            char* str_end;
            auto ll_value = strtoll(val_str, &str_end, 0);
            // was an int.
            if (*str_end == '\0') {
                j_out[key] = ll_value;
            }
        }
        std::cout << j_out.dump() << "\n";
    }
    return 0;
}
