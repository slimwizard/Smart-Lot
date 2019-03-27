usage="test_mode.sh [start|stop]"

if [ $# -eq 1 ]; then
	if [ $1 = "start" ]; then
		echo "test mode starting"
		while true; do
			curl -s -i localhost:5000/smart-lot/test/a19f71fc-4d20-4790-9e38-31df6a02ac76/1 &
			sleep 10
		done
	else
		curl -s -i localhost:5000/smart-lot/test/a19f71fc-4d20-4790-9e38-31df6a02ac76/0 &
	fi
else
	echo "ERROR: expected 1 positional paramter, got $#"
fi

