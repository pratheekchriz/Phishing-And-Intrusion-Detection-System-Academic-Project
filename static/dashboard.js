
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}
function showContent(id) {
  var contentElements = document.querySelectorAll("#main > div");
  for (var i = 0; i < contentElements.length; i++) {
    contentElements[i].style.display = "none";
  }

  document.getElementById(id).style.display = "block";
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));


let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");
let title = document.getElementById("title-menuitem");
let logo = document.getElementById("logo-menuitem");
let icon1 = document.getElementById("icon1");
let icon2 = document.getElementById("icon2");


toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
  title.classList.toggle("titlehide");
  logo.classList.toggle("titlehide");

  if (icon1.style.display === "none") {
    icon1.style.display = "inline-block";
    icon2.style.display = "none";
  } else {
    icon1.style.display = "none";
    icon2.style.display = "inline-block";
  }
};

window.onload = function() {
  var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
  
    data: [{
      type: "pie",
      startAngle: 200,
      yValueFormatString: "##0.00\"%\"",
      indexLabel: "{label} {y}",
      dataPoints: [
        { y: 50.45, label: "Phishing", color: "#f79999"},
        { y: 20.06, label: "Intrusion", color: "#bbd0e7"},
        { y: 40.26, label: "Not detected", color: "#cef8c8"}
      ]
    }]
  });
  chart.render();
};

function addKeyValuePairToSessionStorage() {
  sessionStorage.setItem("role", "admin");

}

function readValueFromSessionStorage() {
  var role = sessionStorage.getItem("role");
  console.log("Role:", role);

  if (role === 'admin') {
    $("#profile-menuitem").hide();
    $("#user-dashboard").hide();

  } else if (role === 'user') {
    $("#user-menuitem").hide();
    $("#password-menuitem").hide();
    $("#admin-dashboard").hide();

  } else {
    console.log('User is a regular user');
  }
}

$(document).ready(function () {
  addKeyValuePairToSessionStorage();
  readValueFromSessionStorage();
  showContent('dashboard');
});





