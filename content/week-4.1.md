Title: Coding Period Week-4 meeting-1
Date: 2021-06-28 18:00-19:00 (IST)
Category: Coding Period
Tags: coding-period, week-4, gsoc-21, fossology, scancode, license-scanner
Author: Sarita Singh
Summary: This is the second of week-4 meeting during coding period. Working on scancode license relevant text highlight.

<h2> Attendees </h2>
<ul> 
<li> <a href="https://github.com/GMishx"> Gaurav Mishra </a>
<li> <a href="https://github.com/mcjaeger"> Michael C. Jaeger</a>
<li> <a href="https://github.com/shaheemazmalmmd"> Shaheem Azmal </a>
<li> <a href="https://github.com/ag4ums"> Anupam Ghosh </a>
<li> <a href="https://github.com/avinal"> Avinal Kumar </a>
<li> <a href="https://github.com/itssingh"> Sarita Singh </a>
</li>
</ul>

<h2> Discussions </h2>
<ul> 
<h3> About Copyright UI (Explained by Gaurav) </h3>
<ul>
<li> Starting with copyright-hist, there are two types of content <code style="color:rgb(14, 149, 233);font-size: 1em;"> statement </code>, coming from the copyright agent and <code style="color:rgb(14, 149, 233);font-size: 1em;">copyFindings </code> which is manual finding added by user form fossology UI.
<li> HistogramBase is the base class for copyright-hist as well as email-hist.
<li> In template there is <code style="color:rgb(14, 149, 233);font-size: 1em;">DataTables</code> plug-in used which add some advanced feature to HTML tables like Pagination, Instant search, sorting, Use almost any data source.
<li> ajax-copyright-hist has collection of functions for different task like update, delete, undo and depending upon the call, function returns <code style="color:rgb(14, 149, 233);font-size: 1em;">JsonResponse</code>.
<li> When there is an API call(GET/POST request), JavaScript functions in the template folder calls ajax and depending upon type of action, ajax fetch data from database and return in JSON response. These JSON responses are rendered on UI.
<li> Like c/cpp main function, FOSSology has <a href= https://github.com/fossology/fossology/blob/master/src/copyright/ui/HistogramBase.php#L187-L287> Output function</a> which defines the entry point. We check in this function that what is the thing that user wants to do.
</ul>
<h3> About Copyright and Author table for ScanCode</h3>
<ul>
<li> Two separate tables would be good.
<li> Number of agent scanning copyright is increasing.
<li> <code style="color:rgb(14, 149, 233);font-size: 1em;">agent_fk</code> in the copyright table is used to  know the version of copyright agent.
<li> Functionality to disable copyright should be there.
<li> Using same table, reporting would be straight away but using different table would be hectic to add reporting.
<li> There would be speed, reporting issues. 
<li> In case of different tables there could be repetition in the copyright data in fossology finding and scancode finding.
<li> Growing data over years could be one of the main reason to keep table separate.
</ul></ul>

<h2> Conclusion </h2>
<ul>
<li> Start with copyright-hist and email-hist then move to ajax and template.
<li> FOSSology uses Output function as the main function(entry point).
<li> In Initial development we can keep separate tables for fossology copyright and scancode copyright, users can select which agent report they want to see. Later on, based on the performance of these agents we can think of removing redundant data by merging these tables or any other idea.
</ul>
