# Website-FileUpDownload-Database
Website built on Python Flask

RUNNING DETAILS:
* In the same folder where app.py is contained, there should be a python virtual environment where you will install any required libraries. This will be a pain to set up if you are new to python's virtual environments. If you make a virtual env in the wrong location, just delete the env and restart. Do NOT attempt to move the env folder's location and think everything will work.

INFO:
* The Database (locally stored) contains the following tables:
  - `jobs`: Tasks to complete
  - `users`: Webpage users who have signed up
  - `files`: Files uploaded by webpage users
  - `results`: Processed files that specific webpage users will download
  - `options`: The ways to deal with a file when processing later. These entries are hardcoded strings.
* The database doesn't exist at first, which is expected and intentional.
  - There's nothing wrong with continuing to use an existing database, AS LONG AS it has fields and table names that match the implementation for every table.
* The program creates the database file and its empty (except for the `options` table) tables when the first user signs up or attempts to log in (even if no users exist at the time), UNLESS the specific tables already exist.
* Once the user submits (uploads) a job, it updates the `files` table and `jobs` table inside the database with the relevant info.
* After the subprocess is spawned (triggered by user submitting ANY file), the subprocess reads the `jobs` table to see if there is a task to run.
  - Subprocess is used (instead of running in the main process) to prevent stalling the main application with the reading of the database
* At the home webpage ('downloads' page), user-submitted files can be downloaded again
  - Useful for comparing the input file to a result file
  
CURRENT BUGS:
* Doesn't check if the job has already completed via the 'complete' field in the 'jobs' table being set to 1.
After the subprocess finishes the job, it creates a result file, updates the 'jobs' table to change the 'complete' field of that particular job to 1, and adds to the 'results' table information about the result file.
* Downloaded files contain a different amount of data and sometimes have unreadable info.
Also at the home webpage, there is supposed to be a retrieval of the results file that you can download.
* There is no accessing the results file(s) from the webpage user's POV.

tl;dr:
* Has working user validation, signup, and login (using the database table)(no duplicate users nor emails). Checks for valid email and nonempty experiment entry (job submission) fields.
* Has file-upload capabilities.
* Has file-download capabilities (serious data-integrity bugs - downloaded files contain different data than what was created).
  
TODO:
* Change hashes to salted hashes. How do I compare them? Prepend to the hash the hashing method used.
* Fix data_write (maybe file read?).
  - Notice how A) png_source_file is different size than the output (i.e., result file) and B) if uploading a text file, then downloading it, there are added characters (b'\n'). 
  - This is possibly a Windows "Carriage Return; Line Feed (\r\n)" vs Everybody else "Line Feed (\n)" issue.
* Display results_picture on website
  - So, will need a separate results page. Might be weird in Flask.
* Submitter can access only their own results from the webpage
  - User A cannot access User B's input files nor results via URL hacking such as changing "usr1/file1" to "usr2/file1"
* Show byte size and simple hash value of user-submitted files
  - So that the user can tell if their submitted file is different than their local file
* Beautify all html pages
  - Use CSS? React? Angular? Idk this frontend stuff yet. Use libraries for better security (and updates to new attack prevention) over time.
