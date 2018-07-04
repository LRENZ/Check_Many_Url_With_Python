# Check_Many_Url_With_Python<br>
Check Many Url With Requests &amp; Output A Result file<br>
Firstly, You Need install mongodb , Cause We Use Mongodb to save all requestsd url & its result<br>
## Uasge: Paste All Url you want to test into(one URL one Line)<br>
     remove.txt    
<br>
and run the script with <br>

     python get_status.py 
 <br>
 if you want to clear all records in database please input  'del'(defalut no_del)<br>
Finaly you will got a file called <br>
    urlcheck.csv
<br>
check whether it's what you want<br>

## Supported features:

* Do not repeatly  request URL, 
* Multi-process support
* Database support
* The result is output as an excel file
 

## How to use:

* Install Python and pip install -r requirement.txt and start mongodb
* Copy the url you want to check into  remove.txt, one url per line
* run get_status.py in  command line . When finished, check the urlcheck.csv result file.

More Detail: [URLCHECK](https://linpiner.com/posts/URL%20%20Checker--%E6%A3%80%E6%9F%A5URL%E7%9A%84Python%E5%B0%8F%E8%84%9A%E6%9C%AC)
