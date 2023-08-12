# roGovWebscraping

## Create a Python script that would scrape the Romanian government's website for the six most recent news articles. The script should download the articles and save them in a JSON file, including the title, text, date of publication, and optionally a summary generated by GPT-4 or GPT-3.5.

### Webpage to scrape: https://gov.ro/en/news

### Expected output:
```json
{
{
        "title": "Prime Minister Marcel Ciolacu: It is particularly useful to have a dynamic process of consultation with representative associations of the young generation",
        "date": "Thursday, 10 August 2023",
        "text": "\nPRESS RELEASE\n\u00a0\n\u00a0Prime Minister Marcel Ciolacu had consultations today with representatives of the European Youth Forum and the Youth Council of Romania, part of the Government\u2019s constant institutional dialogue with representative associations of the social and associative sectors.\n\u201cIt is extremely important to have permanent consultations with young people to bridge\u00a0the gap between generations and particularly between the young generation and stakeholders. Young people have the ability to adapt and rapidly accumulate knowledge\u00a0and information, and to come up with innovative solutions. I noticed how internship programs conducted at the level of Government and Parliament brought\u00a0real benefits not only to young people but also to public institutions. For these reasons, it is particularly useful to have a dynamic process of consultations with representative associations of the young generation\u201d, stated Prime Minister Marcel Ciolacu.\n\u201cWe need vision, commitment, and responsibility on the part of young people, and the fact that we are here together provides us all with a new perspective on the future. Youth\u2019s problems are not few but with the support of Prime Minister Marcel Ciolacu and the Romanian Government, many of them will find a resolution. The new education law comes in support of youth people to create as many opportunities as possible and to strengthen the relationship between the two generations. Together, we will contribute to the growth of the new leaders both at national and European levels\u201d, stated Minister of Family, Youth and Equal Opportunities, Natalia Intotero.\nThe representatives of the European Youth Forum welcomed the good practices existing at the level of the Government, regarding the Official Internship Program, which provides 150 seats\u00a0this year. Interns enrolled in this program receive, according to Law 176/2018 on internships, a monthly allowance representing at least 50% of the minimum gross salary per economy.\nAlso, the representatives of the European Youth Forum showed that there is a need to enhance\u00a0consultations between youth organizations and public authorities, considering that the topic of youth requires an integrated approach at the level of the Government and ministries.\nAttending the discussions, representatives of the Youth Council of Romania appreciated the completion of the National Youth Strategy by the Ministry of Family, Youth, and Equal Opportunities and emphasized the importance of inter-ministerial collaboration to attain the objectives contained in this document.\nAttending the meeting at Victoria Palace alongside Prime Minister Marcel Ciolacu, were the Minister of Family, Youth and Equal Opportunities, Natalia Intotero, the Head of the Prime Minister's Chancellery, Mihai Ghigiu, and the representatives of the Chancellery - Secretary of State Mihai Constantin, State Advisers Ruxandra Ivan and Victoria Stoiciu.\n"
    
}
```

### Regarding openAI optional task, when I try to call the API I get the following error:
$\textcolor{red}{\textsf{You exceeded your current quota, please check your plan and billing details.}}$ 
