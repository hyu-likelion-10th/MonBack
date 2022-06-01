let namebox = document.getElementById("name");

namebox.addEventListener("mouseover", function(e) {
    namebox.innerHTML = 'Lee Subin';
})

namebox.addEventListener("mouseout", function(e) {
    namebox.innerHTML = '이수빈';
})