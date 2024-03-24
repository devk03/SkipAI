function getCookies(domain, name, callback) {
  chrome.cookies.get({ url: domain, name: name }, function (cookie) {
    if (callback) {
      navigator.clipboard.writeText(cookie.value);
      callback(cookie.value);
    }
  });
}
document.addEventListener("DOMContentLoaded", function () {
  var button = document.getElementById("copyCookies");
  button.addEventListener("click", function () {
    getCookies(
      "https://leccap.engin.umich.edu/leccap/player/r/bN2TOQ",
      "AWSALB",
      function (id) {
        alert(id);
      }
    );
  });
});
