mkdir 300W
cd 300W
for i in $(seq -f "%03g" 1 5); do wget https://poc-face-aligment.s3.eu-north-1.amazonaws.com/300W/01_Indoor/indoor_$i.png; done
for i in $(seq -f "%03g" 1 5); do wget https://poc-face-aligment.s3.eu-north-1.amazonaws.com/300W/01_Indoor/indoor_$i.pts; done
cd ..