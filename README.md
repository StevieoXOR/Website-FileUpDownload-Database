# Website-FileUpDownload-Database
Website built on Python Flask

INFO:
The database doesn't exist at first, which is expected and intentional (though there's nothing wrong with continuing to use an existing database, AS LONG AS it has fields that match my implementation for every table). The program creates the database file and its empty (except for the 'options' table) tables when the first user signs up or attempts to log in (even if no users exist at the time), UNLESS the specific tables already exist.
Has jobs table (i.e., tasks to complete), users table (webpage users who have signed up), files table (files uploaded by webpage user), results table (processed files that the webpage user will download).
Once the user submits (uploads) a job, it updates the files table and jobs table inside the database with the relevant info.
After the subprocess is spawned (triggered by user submitting ANY file), the subprocess reads the jobs table to see if there is a task to run
* CURRENT BUG: Doesn't check if the job has already completed via the 'complete' field in the 'jobs' table being set to 1.
After the subprocess finishes the job, it creates a result file, updates the 'jobs' table to change the 'complete' field of that particular job to 1, and adds to the 'results' table information about the result file.
At the home webpage ('downloads' page), user-submitted files can be downloaded again (only really useful for checking the input of a result file).
* Submitter can access only their own results from the webpage
* CURRENT BUG: downloaded files contain a different amount of data and sometimes have unreadable info.
Also at the home webpage, there is supposed to be a retrieval of the results file that you can download.
* CURRENT BUG: There is no accessing the results file(s) from the webpage user's POV.

tl;dr:
Has working user validation, signup, and login (using the database table)(no duplicate users nor emails). Checks for valid email and nonempty experiment entry (job submission) fields.
Has file-upload capabilities.
Has file-download capabilities (serious data-integrity bugs - downloaded files contain different data than what was created).


In the same folder where app.py is contained, there should be a python virtual environment.

TODO:
Change hashes to salted hashes. How do I compare them then?????
Fix data_write (maybe file read?). Notice how A) png_source_file is different size than the output (i.e., result file) and B) if uploading a text file, then downloading it, there are added characters (b'\n').
Display results_picture on website. So, will need a separate results page. Might be weird in Flask.
Beautify all html pages
