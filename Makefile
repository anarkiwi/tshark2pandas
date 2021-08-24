tshark2pandas_jsonfilter: tshark2pandas_jsonfilter.cpp json.hpp
	g++ -O2 -o tshark2pandas_jsonfilter tshark2pandas_jsonfilter.cpp

json.hpp:
	wget -q https://github.com/nlohmann/json/releases/download/v3.10.0/json.hpp

clean:
	@rm -f json.hpp tshark2pandas_jsonfilter
