<html>
  <head><title>IP Information</title></head>
  <body>
    <form action = "/ip" method = "get">
        IP: <input
                name="ip"
                id="ip"
                type="text"
                %if ip_address is not None:
                value="{{ip_address}}"
                %end
            />
        <input
          type="button"
          value="Search"
          onclick="window.location.href=window.location.origin + '/ip/' + document.getElementById('ip').value"
        />
    </form>

    %if result is not None:
        <h2>GeoLocation of given IP:</h2>
        <table border="1">
        %for k, v in result.items():
        <tr>
            <td>{{k}}</td>
            <td>{{v}}</td>
        </tr>
        %end
        </table>
    %end
  </body>
</html>