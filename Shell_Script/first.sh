#!/bin/sh

cd "/home/cupgreek/Deepak_Raghavan/Academics/2019-2020/OOPS/Java"
file_name="$1.java"
touch $file_name
text="class $1{\n\tpublic static void main(String args[]{\n\t\t#Enter your code here\n\t}\n}"
echo $text>>$file_name
nano $file_name
clear

