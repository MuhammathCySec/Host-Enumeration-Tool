import os
import uuid
from datetime import datetime
from jinja2 import Template

from het.utils.logo import HET_LOGO



def generate(data, report_folder):


    # Create report folder
    os.makedirs(
        report_folder,
        exist_ok=True
    )


    report_id = str(uuid.uuid4())[:8]


    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    template = """

<!DOCTYPE html>

<html>

<head>

<title>
HET Security Report
</title>


<style>

body {

background:#0b0f19;
color:white;
font-family:Arial;
padding:30px;

}


.logo {

color:#00ffff;
white-space:pre;
font-size:18px;

}


.card {

background:#151b2b;
padding:20px;
margin:20px 0;
border-radius:15px;

}


table {

width:100%;
border-collapse:collapse;

}


td,th {

border:1px solid #444;
padding:10px;

}


th {

background:#00ffff;
color:black;

}



.low {

color:#00ff00;

}


.medium {

color:#ffff00;

}


.high {

color:#ff3333;

}


</style>


</head>



<body>



<div class="logo">

{{logo}}

</div>



<h1>
HET Security Assessment Report
</h1>



<div class="card">


<b>Report ID:</b>
{{id}}

<br>


<b>Scan Time:</b>
{{time}}


</div>





<div class="card">

<h2>
Security Score
</h2>


<h1 class="{{risk_class}}">

{{score}} / 100

</h1>


<h2>

{{risk}}

</h2>


</div>





<div class="card">


<h2>
System Details
</h2>


<table>


<tr>

<th>
Item
</th>

<th>
Value
</th>

</tr>


{% for key,value in host.items() %}

<tr>

<td>
{{key}}
</td>


<td>
{{value}}
</td>


</tr>


{% endfor %}


</table>


</div>






<div class="card">


<h2>
Network Information
</h2>


<table>


<tr>

<th>
Item
</th>

<th>
Value
</th>

</tr>


{% for key,value in network.items() %}

<tr>

<td>
{{key}}
</td>


<td>
{{value}}
</td>


</tr>


{% endfor %}


</table>


</div>






<div class="card">


<h2>
Security Findings
</h2>


<ul>

{% for item in findings %}

<li>

{{item}}

</li>


{% endfor %}


</ul>


</div>







<div class="card">


<h2>
Recommendations
</h2>


<ul>

{% for item in recommendations %}

<li>

{{item}}

</li>


{% endfor %}

</ul>


</div>






<div class="card">


<h2>
Running Processes
</h2>


<table>


<tr>

<th>
PID
</th>


<th>
Name
</th>


<th>
User
</th>


</tr>


{% for process in processes %}


<tr>


<td>
{{process.pid}}
</td>


<td>
{{process.name}}
</td>


<td>
{{process.username}}
</td>


</tr>


{% endfor %}



</table>


</div>



</body>


</html>


"""



    analysis = data.get(
        "security_analysis",
        {}
    )


    score = analysis.get(
        "security_score",
        0
    )


    risk = analysis.get(
        "risk_level",
        "UNKNOWN"
    )



    if score >= 80:

        risk_class = "low"


    elif score >= 50:

        risk_class = "medium"


    else:

        risk_class = "high"





    html = Template(template).render(


        logo=HET_LOGO,


        id=report_id,


        time=timestamp,


        score=score,


        risk=risk,


        risk_class=risk_class,


        host=data.get(
            "host",
            {}
        ),



        network=data.get(
            "network",
            {}
        ),



        findings=analysis.get(
            "findings",
            []
        ),



        recommendations=data.get(
            "recommendations",
            []
        ),



        processes=data.get(
            "processes",
            {}
        ).get(
            "processes",
            []
        )

    )



    # NEW:
    # Save inside timestamp folder

    report_file = os.path.join(
        report_folder,
        "HET_Report.html"
    )



    with open(
        report_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)



    return report_file