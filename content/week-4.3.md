Title: Coding Period Week-4 meeting-2
Date: 2021-07-02 17:30-18:00 (IST)
Category: Coding Period
Tags: coding-period, week-4, gsoc-21, fossology, scancode, license-scanner
Author: Sarita Singh
Summary: This is the third meeting during coding period. Working on scancode license relevant text highlight.

<h2> Attendees </h2>
<ul> 
<li> <a href="https://github.com/GMishx"> Gaurav Mishra </a>
<li> <a href="https://github.com/avinal"> Avinal Kumar </a>
<li> <a href="https://github.com/itssingh"> Sarita Singh </a>
</li>
</ul>

<h2> Updates </h2>
<ul>
<li> Created scancode_copyright and scancode_author table in the FOSSology database.
<li> Copyright and author information coming from scancode scan result is inserted in these newly created tables.
<li> Improved license data insertion in the license_file and highlight tables by inserting only unique entries based upon rf_fk, agent_fk, and pfile_fk. It solved UI glitch in license relevant text highlighting for scancode.
<li> Latest <a href= https://github.com/itssingh/fossology/commit/c823ecf7a5d59fbfe243281c41598ea161e04435> commit</a> having code to create tables.

</ul>
<h2> Discussions </h2>
<ul>
<li> Using 'S' instead of 'L' for ScanCode type field in the highlight table where 'S' will be match property of the highlight class in HighlightDao.php.
<ul> <li> Added a new type 'S' in the HighlightDao.php also changed type from signature to match as like monk agent ScanCode matches text.
<li> Gaurav explained about identical displayed on the UI by monk scanner as, It highlight those text which are identical with the license text in the license_ref table. Whereas license relevant text means the highlighted text has been matched with license text or rules written for the license. 
<li> So license relevant text is suitable for the ScanCode highlight.
<li> Also Gaurav suggested to reuse the resources already present and no need to add a new type for scancode highlight, nomos type could be reused.
</ul>
<li> Sarita(Me) shows newly created tables for scancode_copyright and scancode_author. Gaurav approved changes.
<li> Added a function in the scancode database to insert no license in the license_file table for a code zip have no license.

```cpp
bool ScancodeDatabaseHandler::insertNoResultInDatabase(int agentId, long pFileId )
{
  return saveLicenseMatch(agentId, pFileId, 320, NULL);
}
```
<ul>
<li> Gaurav clarified that '320' is not constant licenseId for no-license. So instead leave licenseId null. 
<li> There is still a discussion needed (with other mentors) to decide is no license case is needed to take care for ScanCode or not.
</ul>
<h2> Upcoming Plans </h2> 
<ul> 
<li> Start implementing UI to make scancode a parameterized agent.
<li> Discuss about no license/copyright/author case for scancode.
</ul>