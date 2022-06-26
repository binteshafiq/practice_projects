%# disp_table.tpl
<p>GeoLocation of given IP:</p>
<table border="1">
%for r in rows:
  <tr>
    <td>{{r}}</td>
    <td>{{rows[r]}}</td>
  </tr>  
%end
</table>