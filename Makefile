tshark2pandas_jsonfilter: tshark2pandas_jsonfilter.cpp json.hpp
	g++ -O2 -o tshark2pandas_jsonfilter tshark2pandas_jsonfilter.cpp

json.hpp:
	wget -q https://raw.githubusercontent.com/nlohmann/json/develop/single_include/nlohmann/json.hpp

clean:
	@rm -f json.hpp tshark2pandas_jsonfilter
