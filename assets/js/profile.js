$(document).ready(function () {
  $.ajax({
    type: "POST",
    url: "auth_status.php",
    datatype: "html",
    data: {
      username: localStorage.username,
      auth_token: localStorage.auth_token,
    },
    success: function (response) {
      var parsedResponse = JSON.parse(response);
      if (parsedResponse != "false") {
        document.getElementById("name").innerHTML = parsedResponse.name;
        document.getElementById("username").innerHTML = parsedResponse.username;
        document.getElementById("email").innerHTML = parsedResponse.email;
        document.getElementById("ph_no").innerHTML = parsedResponse.ph_no;
      } else {
        window.location.pathname = "/logout.html";
        localStorage.clear;
      }
    },

    error: function (error) {},
  });
});
