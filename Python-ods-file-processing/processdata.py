
import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
###  data processing
#######################################################
print("content[0]:",contents[0])
print("Content[0][0]:",contents[0][0])
print("type of content[0][0]:",(type(contents[0][0])))
print("cell at index 4,0:",contents[4][0])
print("cell at index[5][1]:",contents[5][1])
a=int(contents[0][2])+int(contents[1][2])
print("sum of [0][2] and[1][2]:",a)
print("""          ###########################################################################
     ###THIS IS ORIGINAL DATA TABLE AND WE WILL DO SOME CALCULATIONS ACCORDING TO TABLE###
          ###########################################################################
         Month	   General Cargo (Short Tons)	2010

         January	  Container	                1182992
                      Breakbulk 	            15563
	                  Total General Cargo	    1198555

         February	  Container	                1320745
	                  Breakbulk	                18320
	                  Total General Cargo	    1339065

         March	      Container	                1406822
	                  Breakbulk	                20324
	                  Total General Cargo	    1427146

         April	      Container	                1243767
	                  Breakbulk	                14996
	                  Total General Cargo	    1258763

         May	      Container	                1322713
                	  Breakbulk	                26337
                	  Total General Cargo    	1349050

         June	      Container	                1278371
	                  Breakbulk	                22627
	                  Total General Cargo	    1300998

         July	      Container 	            1209612
	                  Breakbulk             	23425
	                  Total General Cargo	    1233037

         August	  Container	                    1224728
	                  Breakbulk	                23353
	                  Total General Cargo	    1248081

         September	  Container	                1121796
	                  Breakbulk	                11957
	                  Total General Cargo	    1133753

         October	  Container	                1330334
	                  Breakbulk	                33449
	                  Total General Cargo	    1363783

         November	  Container	                1303797
	                  Breakbulk             	14393
	                  Total General Cargo	    1318190

         December	  Container	                1123171
	                  Breakbulk	                29110
	                  Total General Cargo	    1152281

   """)

b=int(contents[2][2])+int(contents[5][2])+int(contents[8][2])+int(contents[11][2])+int(contents[14][2])+int(contents[17][2])+int(contents[20][2])+int(contents[23][2])+int(contents[26][2])+int(contents[29][2])+int(contents[32][2])+int(contents[35][2])
print("TOTAL BREAKBULK:",b,end='\t\t\t\t\t\t')
c=b/12
print("AVERAGE BREAKBULK IN A MONTH:",c)

d=int(contents[1][2])+int(contents[4][2])+int(contents[7][2])+int(contents[10][2])+int(contents[13][2])+int(contents[16][2])+int(contents[19][2])+int(contents[22][2])+int(contents[25][2])+int(contents[28][2])+int(contents[31][2])+int(contents[34][2])
print("TOTAL CONTAINER:",d,end='\t\t\t\t\t')
f=d/12
print("AVERAGE CONTAINER IN A MONTH:",f)
g=int(contents[3][2])+int(contents[6][2])+int(contents[9][2])+int(contents[12][2])+int(contents[15][2])+int(contents[18][2])+int(contents[21][2])+int(contents[24][2])+int(contents[27][2])+int(contents[30][2])+int(contents[33][2])+int(contents[36][2])
print("TOTAL GENERAL CARGO:",g,end='\t\t\t\t')
h=g/12
print("AVERAGE GENERAL CARGO IN A MONTH:",h,end='\n\n')


k=1
while k==1:
    sss=input("WHICH AVERAGE IS MORE THAN THE OTHER?(ANSWER WITH SMALL LETTERS PLEASE)=")
    if sss=="container":
        print("! YOU ARE RIGHT..CONTAINER AVERAGE IS MORE THAN BREAKBULK!")
        k=0
    elif sss=="breakbulk":
        print("!YOU ARE WRONG TRY AGAÝN")
    else:
        print("GIVE ME THE REAL ANSWER!!!")

#htmlhtmlhtmlhtmlhtmlhtmlhtmlhtmlhtmlhtmlthmtlhtmlhtmlhtmlhtmlhtml

import webbrowser
f = open('a2_output.html','w')
message = """<!DOCTYPE html>
<html>
    <head>
       <title>TONS OF CARGO(2010)</title>
       <h1 align="center" style="color:#FFFFCC;margin-top:25px;">TONS OF CARGO IN 2010 </h1>
        <meta charset="utf-8" />
        <style>
              td {
                  border: 1px solid black;
                  padding: 5px;
              }
        </style>
    </head>
   <body background="resim.jpg"><table width="394" border="0">
  <tr>
    <th width="191" scope="col"><p>
  <table cellspacing="0" border="0" style="margin-left:365px;">
  <colgroup width="113">
  </colgroup>
  <colgroup width="291">
  </colgroup>
  <colgroup width="96">
  </colgroup>
  <tr>
    <td height="20" align="center" bgcolor="#999999"><strong><em>Month</em></strong></td>
    <td align="center" bgcolor="#999999"><strong><em>General Cargo (Short Tons)</em></strong></td>
    <td align="center" bgcolor="#999999" sdval="2010" sdnum="3081;"><strong><em>2010</em></strong></td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">January</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1182992" sdnum="3081;">1182992</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="15563" sdnum="3081;">15563</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1198555" sdnum="3081;">1198555</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">February</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1320745" sdnum="3081;">1320745</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="18320" sdnum="3081;">18320</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1339065" sdnum="3081;">1339065</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">March</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1406822" sdnum="3081;">1406822</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="20324" sdnum="3081;">20324</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1427146" sdnum="3081;">1427146</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">April</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1243767" sdnum="3081;">1243767</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="14996" sdnum="3081;">14996</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1258763" sdnum="3081;">1258763</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">May</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1322713" sdnum="3081;">1322713</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="26337" sdnum="3081;">26337</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1349050" sdnum="3081;">1349050</td>
  </tr>
  <tr>
    <td height="20" align="center" bgcolor="#999999">June</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1278371" sdnum="3081;">1278371</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="22627" sdnum="3081;">22627</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1300998" sdnum="3081;">1300998</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">July</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1209612" sdnum="3081;">1209612</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="23425" sdnum="3081;">23425</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1233037" sdnum="3081;">1233037</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">August</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1224728" sdnum="3081;">1224728</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="23353" sdnum="3081;">23353</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1248081" sdnum="3081;">1248081</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">September</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1121796" sdnum="3081;">1121796</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="11957" sdnum="3081;">11957</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1133753" sdnum="3081;">1133753</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">October</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1330334" sdnum="3081;">1330334</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="33449" sdnum="3081;">33449</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1363783" sdnum="3081;">1363783</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">November</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1303797" sdnum="3081;">1303797</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="14393" sdnum="3081;">14393</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1318190" sdnum="3081;">1318190</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999">December</td>
    <td align="center" bgcolor="#999999">Container</td>
    <td align="center" bgcolor="#999999" sdval="1123171" sdnum="3081;">1123171</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Breakbulk</td>
    <td align="center" bgcolor="#999999" sdval="29110" sdnum="3081;">29110</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#999999"><br></td>
    <td align="center" bgcolor="#999999">Total General Cargo</td>
    <td align="center" bgcolor="#999999" sdval="1152281" sdnum="3081;">1152281</td>
  </tr>
</table>&nbsp;</p>
    <p>&nbsp;</p></th>
    <th width="187" scope="col">
    <table cellspacing="0" border="0">
  <colgroup width="85">
  </colgroup>
  <colgroup width="175">
  </colgroup>
  <colgroup width="201">
  </colgroup>
  <tr>
    <td colspan="3" height="20" align="center" bgcolor="#EEEEEE"><strong><em>MONTHLY BREAKBULK  (ASC.)</em></strong></td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">September</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="11957" sdnum="3081;">11957</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">November</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="14393" sdnum="3081;">14393</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">April</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="14996" sdnum="3081;">14996</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">January</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="15563" sdnum="3081;">15563</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">February</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="18320" sdnum="3081;">18320</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">March</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="20324" sdnum="3081;">20324</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">June</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="22627" sdnum="3081;">22627</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">August</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="23353" sdnum="3081;">23353</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">July</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="23425" sdnum="3081;">23425</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">May</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="26337" sdnum="3081;">26337</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">December</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="29110" sdnum="3081;">29110</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">October</td>
    <td align="center" bgcolor="#EEEEEE">Breakbulk</td>
    <td align="center" bgcolor="#EEEEEE" sdval="33449" sdnum="3081;">33449</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">TOTAL</td>
    <td align="center" bgcolor="#EEEEEE">BREAKBULK</td>
    <td align="center" bgcolor="#EEEEEE" sdval="253854" sdnum="3081;">253854</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#EEEEEE">AVERAGE</td>
    <td align="center" bgcolor="#EEEEEE">BREAKBULK</td>
    <td align="center" bgcolor="#EEEEEE" sdval="21154.5" sdnum="3081;">21154.5</td>
  </tr>
</table>&nbsp;
<table cellspacing="0" border="0">
  <colgroup width="85">
    </colgroup>
  <colgroup width="175">
    </colgroup>
  <colgroup width="201">
    </colgroup>
  <tr>
    <td colspan="3" height="17" align="center" bgcolor="#CFE7F5"><strong><em>MONTHLY GENERAL CARGO(ASC.)</em></strong></td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">September</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1133753" sdnum="3081;">1133753</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">December</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1152281" sdnum="3081;">1152281</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">January</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1198555" sdnum="3081;">1198555</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">July</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1233037" sdnum="3081;">1233037</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">August</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1248081" sdnum="3081;">1248081</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">April</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1258763" sdnum="3081;">1258763</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">June</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1300998" sdnum="3081;">1300998</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">November</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1318190" sdnum="3081;">1318190</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">February</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1339065" sdnum="3081;">1339065</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">May</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1349050" sdnum="3081;">1349050</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">October</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1363783" sdnum="3081;">1363783</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">March</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1427146" sdnum="3081;">1427146</td>
  </tr>
  <tr>
    <td height="17" align="left" bgcolor="#CFE7F5">TOTAL </td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="15322702" sdnum="3081;">15322702</td>
  </tr>
  <tr>
    <td height="17" align="center" bgcolor="#CFE7F5">AVERAGE</td>
    <td align="center" bgcolor="#CFE7F5">Total General Cargo</td>
    <td align="center" bgcolor="#CFE7F5" sdval="1276891.83333333" sdnum="3081;">1276891.83333333</td>
  </tr>
</table>
<p>
<table cellspacing="0" border="0">
  <colgroup width="85">
  </colgroup>
  <colgroup width="175">
  </colgroup>
  <colgroup width="201">
  </colgroup>
  <colgroup width="85">
  </colgroup>
  <tr>
    <td colspan="3" height="17" align="left" bgcolor="#FFFFCC">TOTAL GENERAL CARGO NUMBER</td>
    <td align="center" bgcolor="#FFFFCC" sdval="12" sdnum="3081;">12</td>
  </tr>
  <tr>
    <td colspan="3" height="17" align="left" bgcolor="#FFFFCC">TOTAL CONTAINER NUMBER</td>
    <td align="center" bgcolor="#FFFFCC" sdval="12" sdnum="3081;">12</td>
  </tr>
  <tr>
    <td colspan="3" height="17" align="left" bgcolor="#FFFFCC">TOTAL BREAKBULK NUMBER</td>
    <td align="center" bgcolor="#FFFFCC" sdval="12" sdnum="3081;">12</td>
  </tr>
  <tr>
    <td colspan="3" height="17" align="left" bgcolor="#FFFFCC">TOTAL BREAKBULK MORE THAN 20K</td>
    <td align="center" bgcolor="#FFFFCC" sdval="178625" sdnum="3081;">178625</td>
  </tr>
  <tr>
    <td colspan="3" height="17" align="left" bgcolor="#FFFFCC">TOTALCONTAINER MORE THAN 2M</td>
    <td align="center" bgcolor="#FFFFCC" sdval="0" sdnum="3081;">0</td>
  </tr>
  <tr>
    <td colspan="3" height="17" align="left" bgcolor="#FFFFCC">NUMBER OF TOTAL CARGO MORE THAN 20M</td>
    <td align="center" bgcolor="#FFFFCC" sdval="0" sdnum="3081;">0</td>
  </tr>
</table></p></th>
  </tr>
  <tr>
    <th scope="row">&nbsp;</th>
    <td>&nbsp;</td>
  </tr>
</table>
<p style="color:#00FFFF; margin-left:110px;">THESE ARE THE TABLES ACCORDING TO TONS OF CARGOS IN 2010.RIGHT SIGHT OF THE PAGE THAT SMALL TABLES ARE MY CALCULATIONS.I MADE IT AS MY ODS FILE AND ADDED DIFFERENT TABLES.
 </p>
</body>
</html>

"""

f.write(message)
f.close()

webbrowser.open_new_tab('a2_output.html')




