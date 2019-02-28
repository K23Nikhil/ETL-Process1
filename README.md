# ETL-Process1
In ETL process is must to understand the extract the data from source system in any format and write into data wharehouse.
Python script to extract the data from sql server and write in xml format

We can extract the data from source system and write data in our system on batch basis. 
We can schedule the python script file using Windows Task scheduler. We cand o the same on linux as well.

Open Task Schedule > 
         Scheduler Name
•	Action > to check python path run on CMD
python -c "import sys; print(sys.executable)"  #In my case C:\Program Files\Python37\python.exe
Add Arguments: Python Script File Name i.e. Script1.py
Start In  Python Script File Path
 i.e. C:\Users\Nikhil Kulshrestha\source\repos\SelectionOfSubsetOfData\pythonPractice
•	Triggers -> As per your need schedule your script on daily basis

Final Output will get like thi. It's just sample data.

<Data>
	<Row stcode="'000001' "/>
	<Row stcode="'000002' "/>
	<Row stcode="'000003' "/>
</Data>

