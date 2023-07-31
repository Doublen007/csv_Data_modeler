# csv_Data_modeler
A Python function designed to easily model data from an excel file.

The function currently reads from an excel sheet. Excel already has a built in feature that can pull data from a csv or space seperated value sheet like a text document into an excel table.

To call the function, filename / filepath should lead to an excel spreadsheet. x and y parameters are the column titles verbatum. Comments with asterisks are for users to adjust.

Currently I've been using this function to graph data from mad star Mesa stellar evolution code, (http://user.astro.wisc.edu/~townsend/). I wanted to share this with the community because I felt like there weren't any resources to graph simulation data from mad star EZ-Web, especially the column data.

I've included an empty excel sheet with column titles for the stellar evolution code because the text document from mesa doesn't include column titles. You can import the mad star data as a csv in excel.
I've also included a sample of some mad-star data in summary2.xlsx with corresponding parameter inputs on the bottom of the python program.

Hope this helps someone! Happy Coding :)
