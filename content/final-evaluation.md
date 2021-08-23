Title: Final Evaluation
Date: 2021-08-23
Category: Final evaluation
Tags: gsoc-21, fossology, scancode
Author: Sarita Singh

### Final Evaluation Report GSoC'21

<h5> Organization: FOSSology </h5>
<h5> Project: Integrating ScanCode Toolkit to FOSSology </h5>
<h5> Mentor:<a href="https://github.com/mcjaeger"> Michael C. Jaeger</a>, <a href="https://github.com/GMishx"> Gaurav Mishra </a>, <a href="https://github.com/hastagAB"> Ayush Bhardwaj</a>, <a href="https://github.com/sjha2048"> Sahil Jha</a></h5>
<h5> Student: <a href="https://github.com/itssingh"> Sarita Singh</a></h5>


### Source Code (GitHub)

- [GSoC Pull Request](https://github.com/fossology/fossology/pull/2074)
- [Branch I was working during GSoC](https://github.com/itssingh/fossology/commits/feat/newagent/scancode-toolkit)


### Related Blog Posts

- [FOSSology Official Blog](https://fossology.github.io/gsoc/docs/2021/scancode/)
- [Wiki](https://github.com/itssingh/fossology/wiki)
- [Personal Blog](https://itssingh.github.io/gsoc-blog/)


## Description

Integrating ScanCode toolkit as a new agent to FOSSology. Using the command line interface from the scancode package in order to be called right from the fossology application. Fossology is passing a single file and takes the result for <code style="color:rgb(14, 149, 233);font-size: 1em;">license/copyright/author</code> from the scancode command line call.


### Current Status

   | category | task | status |
   |----------|------|--------|
   |template|Using scancode custom template| &#9745; |
   |license| License info scanned by scancode | &#9745; |
   |license DB|Reusing existing license in the fossology database| &#9745;|
   |license DB|Inserting new license in the fossology database| &#9745; |
   |license UI|Highlighting license relevance text| &#9745; |
   |license DB|Inserting new license key,full name, ref_url| &#9745; | 
   |license DB|Inserting license text for new license in fossology| &#9744; |
   |license report|Including scancode in the license report| &#9745;|
   |copyright|Creating new tables for copyright and author both on UI and DB| &#9745; |
   |copyright|Copyright and Author info scanned by scancode| &#9745; |
   |copyright|Email and URL info scanned by scancode| &#9744; |
   |copyright DB|Populated newly created scancode database table| &#9745; |
   |copyright UI|Copyright bulk view has scancode table populated| &#9745; |
   |copyright UI|Email/URL/Author bulk view has scancode table populated| &#9745; |
   |copyright UI|Copyright single view has scancode integrated| &#9745; |
   |copyright UI|Highlight working for copyright| &#9744;|
   |copyright report|Including scancode copyright in the report| &#9744;|
   |scancode|Schedule scancode from bulk view space |&#9744;|
   |API|Integrating ScanCode to FOSSology API |&#9745;|
   |testing|Write tests for scancode agent|&#9744;|
   |CLI|Using CLI to run scancode|&#9744;|

### Video Demonstration

[Demonstrating ScanCode integrated to the FOSSology UI](https://youtu.be/QJ6myDUbkwI)


### Working

- Scancode is a parametric agent which can provide information regarding license, copyright, Email, and URL information separately or all together.
- When a user uploads a file, Scheduler passes a single file and takes the result for license/copyright/author from the scancode command line call. These results are stored in the FOSSology database depending upon the kind of result.
    - Licenses are stored in the license_file table based on the agentId, pfileId, and rf_fk.
    - New licenses are inserted into the license_ref table.
    - Highlight table is used to save highlight info.
    - There are scancode_copyright and scancode_author tables to save scancode findings for copyright and Author respectively. Also, both have event tables to store scanner deactivated statements.
- These data are rendered on UI in respective fields:
    - For license information check License Browser.
    - For Copyright information check copyright tab.
    - For Author information check Email/URL/Author tab.


### Challenges

- Understanding existing codebase for such a large project, I had to make changes in new code as well as existing code so understanding code and making changes and debugging that was quite challenging.
- Working on a full stack project, I had to learn new tech-stack quickly to complete task before deadline. 


### Learnings

- Worked on a full stack project.
- Got to learn so many new tech- stack like PHP, Rest API, Database, Docker, OOPs (Full of learning).
- Got chance to improve my communication skills.
- Learned how to work and interact in a community.
- Got chance to interact with peers, mentors.


### How to test

- Fetch [sarita/newagent/scancode](https://github.com/itssingh/fossology/tree/sarita/newagent%2Fscancode) on your local by using command <code style="color:rgb(14, 149, 233);font-size: 1em;">$ git fetch https://github.com/itssingh/fossology sarita/newagent/scancode:scancode</code> and checkout to the <code style="color:rgb(14, 149, 233);font-size: 1em;">scancode</code> branch.
- [Install FOSSology from source](https://github.com/fossology/fossology/wiki/Install-from-Source)
- Upload a file from Source/URL/VCS then select license or copyright under scancode-toolkit.

    *NOTE:* Email and URL are not working for now as scancode-toolkit doesn't provide this info by using a custom template ([PR](https://github.com/nexB/scancode-toolkit/pull/2539) is merged waiting for new release 🥳 ).

    - Check license browser/license single file view for license information.
    - Check copyright bulk view or copyright single view for copyright information.
    - Check author/email/URL bulk view.

- If you are facing a problem in installing scancode, please install the scancode-toolkit manually. The steps to [install scancode-toolkit](https://github.com/itssingh/fossology/wiki/scancode#the-steps-to-install-scancode-toolkit)


### Open Source Contributions
- [FOSSology Project](https://github.com/fossology/fossology/pulls?q=author%3Aitssingh+)
- [FOSSology GSoC](https://github.com/fossology/gsoc/pulls?q=author%3Aitssingh+)
- [ScanCode Toolkit](https://github.com/nexB/scancode-toolkit/pulls?q=author%3Aitssingh+)
- [All PRs](https://github.com/pulls?q=is:pr+author:itssingh)

### Resources
- [ScanCode Toolkit documentation](https://scancode-toolkit.readthedocs.io/en/latest/)
- [FOSSology](https://github.com/fossology/fossology)
- [ScanCode Toolkit](https://github.com/nexB/scancode-toolkit)
