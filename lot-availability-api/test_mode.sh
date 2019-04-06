usage="test_mode.sh [start|stop]"
echo "test mode starting"
while true; do
	curl -s -i localhost:5000/smart-lot/test/a19f71fc-4d20-4790-9e38-31df6a02ac76/1 &
	sleep 10
done
