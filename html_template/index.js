function appendData(inf) {
  fetch("../info.json")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      var prueba = "dg";
      document.getElementById(inf).innerHTML = data["info"][inf];
      console.log(data);
    });
}

function appendToday() {
  var today = Date.now();
  var addToday = today.toLocaleDateString();
  document.getElementById("today").innerHTML = "dfsd";
}
