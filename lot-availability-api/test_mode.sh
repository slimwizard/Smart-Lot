usage="test_mode.sh [start|stop]"

if [ $# -eq 1 ]; then
	if [ $1 = "start" ]; then
		echo "test mode starting"
		while true; do
			curl -s -i localhost:5000/smart-lot/test/1 &
			sleep 20
		done
	else
		curl -s -i localhost:5000/smart-lot/test/0 &
	fi
else
	echo "ERROR: expected 1 positional paramter, got $#"
fi

