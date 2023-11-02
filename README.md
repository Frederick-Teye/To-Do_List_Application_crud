# To-Do_List_Application_crud

Project Name: To Do List Console Application

Introduction: This project is done to solidify my understanding of CRUD in sql(sqlite).
I have used all the CRUD(Create Read Update and Delete) operations in this application.
This application only uses date to track and record all todo items. It did not use time
and does not have notification, because that would have better been done with a GUI.

PROJECT OVERVIEW
Description: The application is having 24 function(including the main functions). All of
these functions have a specific roll they play. Let us get into each function and the 
role that they play:

1. main()
When the application is first run and the database file does not exist, the main function
creates it and if the database file exists, the dates and status of each to do item in
the database is updated by calling our second function.

2. update_status()
This function is called in main function and also whenever a date of a to do item is
changed, it also get called. It main purpose is to update dates and status of the to-do
item. If the current day is the day that the to-do item needs to get completed, it will
update it to 'In progress', if the day that the item supposed to be completed have pass,
it update it to 'Overdue' and when the day have not gotten to yet, it keep it at pending.
This function do not update the status of any to-do item that has a status marked 
'completed'.

3. menu()
The menu function help the use to interact with the whole application or navigate through
it. 

4. item_status()
This function takes the days left for a to-do item and set it status to 'In progress',
'Pending' or "Overdue".

5. days_lft()
This function calculates the days left or overdue of a todo item.

6. item_status_number()
This function takes the status of an item as an argument and provide it status number. I
planned to use the status number when I was designing the application on paper without
writing the code yet, but when I started writing the code, I decided to leave that out.

7. add_new_item()
As it names sounds, this function helps the user to add a new item to the application. It
calls all the former functions when needed.

8. get_due_date()
This function help the application to get a date from the user. It is called in the 
add_new_item() function and also update_date() function. This function calls our next 
function because it could perform the function that the next function performs inside it.
What is the next function?

9. get_month()
This function is called by the get_due_date function to get the month from the user, and
it does just exactly that. It return the month to the get_due_date() function.

10. view_items()
This function helps the user to view all items in the database.

11. view_an_item()
This function helps the user to view an item in the database. It is called by all function
that updates a value in the database or deletes a row in the database. This function
calls other functions when performing it operations and those function are: 
view_by_desc() function, view_by_priority() function, and view_by_status() function.

12. update_a_list_item()
This functions helps the user to update a value of a list item. It calls the following
functions in it's operations: update_description(), update_due_date(), 
update_priority() and mark_status_complete().

13. delete_item()
This function help the user to delete an item in the database table or all the items in
the database table. It does that by calling delete_an_item() function and 
delete_all_items() functions.

14. delete_an_item()
This function calls the view_an_item() function and make the user view the item that
he/she/they want to delete and then ask the user to enter the id after that. It ask the
user again to confirm if they really want to delete the item in the database and if the
user answer yes, it deletes the item in the database.

15. delete_all_items()
As it name sounds, it deletes all items in the database table. It ask the user twice to
to confirm if they want to delete all items in the database, and if the user answer all
yes, it goes ahead to delete all the data in the database.

16. exit_application()
This function helps the user to exit the application with a goodbye message.

17. get_description()
This function gets a description of a to-do item that is less than 25 characters from the
user. If the description is more than the 25 characters, it edits it and ask the user if
they are okay with it, if the user says yes, then it returns that description to wherever
it have been called. This is called by update_description() and add_new_item()

18. update_description(args)
This function takes id of a data in the database table and updates it description.

19. update_due_date(args)
This function takes id of a data in the database table and updates it date after that
it calls update_status() so that it updates the status of the data if needed.

20. update_priority(args)
This function helps the user updates the priority of a data in the database table.

21. mark_status_completed(args)
It helps the user to mark the status of a data in the table 'Completed'.

22. When I count the function, they are 24, but the ones that I have explained their
functionality are only 21. I tried counting again and their 24, anyway, the names of the
functions are descriptive and the codes are not ambiguous.


Finally, I want to say that it is easy to navigate through the application. Just take
your time and read the instructions. I am open to corrections. I try hard a do a graphical
user interface of it with Java. And maybe I will do one code on relational data with
Java. This is because GUI with Java makes sense that GUI with python, because I don't 
think I will ever be using python to create a GUI application. Thank you very much for
reading all this, I promise to do more sophisticated staff in the future. One Love <3