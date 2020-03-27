#!/bin/bash

echo" Select an option: "
echo"1) CPU information"
echo"2) List Device drivers"
echo"3) Load average"
echo"4) display PID and PPID of a process"
echo"5) exit"

read choice

if [choice = "1"]
then
	echo"CPU Info"
	cat /proc/cpuinfo



