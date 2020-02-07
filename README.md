# pyQtmonRep

PyQt5 GUI for kmpeters monthlyReport Python program 
Work in progress ; current functionality outlined below.

The GUI can open existing monthly report XML file and display in a table.
In the text entry box, enter the filename of the existing XML file to be opened (file must be in the same directory as the script).
Click the "Enter" button, followed by the "log2df" button. Creates a pandas data frame object and displays to table.
Table is superficially editable; double clicking a table cell allows user to change the text, 
but currently the delegate mechanism is not in place to save the data back to the underlying XML.

If user enters a filename that does not exist, prompts user to create a new file.
File is created, but no other functionality is implemented yet.
