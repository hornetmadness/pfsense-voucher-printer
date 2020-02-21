from string import Template

MAIN_HTML = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Print Vouchers</title>
  <style>
    html, body {
      height: 100%;
      width: 100%;
      margin: 25;
      padding: 10px;
      justify-content: left;
      align-items: left;
      font-size: 24pt;
    }
    .button {
      box-shadow: 3px 4px 0px 0px #8a2a21;
      background:linear-gradient(to bottom, #c62d1f 5%, #f24437 100%);
      background-color:#c62d1f;
      border-radius:18px;
      border:1px solid #d02718;
      display:inline-block;
      cursor:pointer;
      color:#ffffff;
      font-family:Arial;
      font-size:48px;
      padding:7px 25px;
      text-decoration:none;
      text-shadow:0px 1px 0px #810e05;
    }
    .button:hover {
      background:linear-gradient(to bottom, #f24437 5%, #c62d1f 100%);
      background-color:#f24437;
    }
    .button:active {
      position:relative;
      top:1px;
    }
  </style>
</head>
<body>
  <ul style="list-style-type:none;">
  ${list_html}
  </ul>
</body>
</html>
""")

BUTTON_HTML = Template("""
  <button class="button", onclick="window.location.href = 'my.bluetoothprint.scheme://${print_url}'">${time} Minute Voucher</button>
""")

def render(print_url, times):
  thelist = ""
  for time in times:
    itemtxt="<li>"
    itemtxt+=f"<h3>Remaining: {time[1]}</h3>"
    p=f"{print_url}?time={time[0]}"
    itemtxt += BUTTON_HTML.substitute(print_url=p, time=time[0])
    itemtxt +=" </li>"
    thelist += itemtxt

  if not thelist:
    thelist = "<li> <h3>No active vouchers found in the DB</h3> </li>"
  return MAIN_HTML.substitute(list_html=thelist)