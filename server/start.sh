#! /bin/bash
echo "CED_KEY Server Starting..."
cd /home/pi/ced_key/server
echo "Waiting Network Connection..."
retry=10

for i in `seq $retry`; do 
  _IP=$(hostname -I) || true
  if [ "$_IP" ]; then
    echo $_IP
    break
  fi  
  sleep 1
done

python ./main.py > ./server.log 2>&1 &
echo "Begin to watch update of Google Spread Sheet"
