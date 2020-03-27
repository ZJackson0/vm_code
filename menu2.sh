

echo "1. CPU Information" 
echo "2. List Device drivers" 
echo "3. Load average"
echo "4. display PPID of a process"
echo "Q.Quit" 
echo 
echo "Enter choice" 

read choice 

case $choice in
	1) echo "Displaying CPU Info"
	cat /proc/cpuinfo 
	;;

	2) echo "Device Drivers"
	cat /proc/devices
	;;

	3) echo "Displaying load average"
	cat /proc/loadavg
	;;

	4) echo "Enter the PID"
	read pid
	cat /proc/${pid}/status | grep -e "PPid"
	;;

	q) echo "Exiting "
	exit
	;;

esac