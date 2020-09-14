# Code for the JustOn challenge

## How-To
 * At the moment the only way to enter data is to have the data.json in the same directory as the app.py source file.

 * The requested actions on the dictionary are then perfomed when prompting the GET method via

curl -i http://host_address/db/dict/entry_00

 * Further development would be required:
   * Add exception when the data does not contain the required fields
   * Allow for multiple dictionaries to be stored / modified adding PUT and POST methods

