Title: Community Bonding Period Meeting-2
Date: 2021-06-04 17:00-18:00 (IST)
Category: Community-Bonding
Tags: community-bonding, gsoc-21, fossology, scancode, license-scanner, ojo, decider
Author: Sarita Singh
Summary: This is the second meeting during community bonding period.

<h2> Organiser </h2>
<ul> <li> <a href="https://github.com/GMishx"> Gaurav Mishra </a> </li> </ul>

<h2> Attendees </h2>
<ul> 
<li> <a href="https://github.com/GMishx"> Gaurav Mishra </a>
<li> <a href="https://github.com/ag4ums"> Anupam Ghosh </a>
<li> <a href="https://github.com/avinal"> Avinal Kumar </a>
<li> <a href="https://github.com/itssingh"> Sarita Singh </a>
</li>
</ul>

<h2> Discussion </h2>
<ul>
<h3> <strong> About the current update </strong> </h3>
<ul> 
<li> ScanCode <a href= https://gist.github.com/itssingh/93db537d2a9c9a6780a71cd84a41c6ab\> custom output </a> for license, copyright and holders is working 
<li> Currently scancode doesn't support emails and urls custom output.
<li> Opened a pr for <a href= https://github.com/nexB/scancode-toolkit/pull/2539> this </a>
</ul>
<h3> <strong> About the DatabaseHandler </strong> </h3>
<ul> 
<li> Gaurav explained how <a href= https://github.com/fossology/fossology/blob/master/src/ojo/agent/OjosDatabaseHandler.cc> ojos databasehandler </a> workes.
<ul>
<li> Convert shortname to lower-case
<li> Remove last occurrence of + and -or-later 
<li> Remove last occurrence of -only
</ul>
<li> Similar approach can work for license spdx key <a href= https://docs.google.com/spreadsheets/d/1lgAVHofEXyVLa7ocrl8rGjuNulY7VgF-WGOQVqYkmoE/edit#gid=680720653> differnece </a> in scancode and fossology database
</ul>
<h3> <strong> About the UI </strong> </h3>
<ul> 
<li> ScanCode simple UI (License integration) will resemble more with ojo 
<li> When it will be parametrized( copyrights, emails, urls along with license),
It will resemble closely with decider UI
<li> When scancode UI will have licenses, coyright, email, urls options then user can select more than one options at once.
write a plugin containg a switch case will give execute based on the options selected. Decider uses <a href= https://github.com/fossology/fossology/blob/master/src/decider/ui/DeciderAgentPlugin.php#L75-L126> this </a>.
</ul></ul>
<h2> Conclusion and upcoming plans </h2> 
<ul>
<li> Scancode Jinja template is working for license and copyright.
<li> Start working on scancode integration for license scanning.
<li> There would be a meet at May 7, 2021.
<li> Fork and create a branch for development and mention the same in blog/wiki <a href= https://github.com/itssingh/fossology/wiki> done </a>
<li> Add a timeline section in blog/wiki as provided in the project proposal <a href= https://itssingh.github.io/gsoc-blog/timeline.html> done </a>
</ul>
